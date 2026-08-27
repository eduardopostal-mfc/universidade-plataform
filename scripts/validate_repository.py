#!/usr/bin/env python3
"""Valida a estrutura pública e os cronogramas dos projetos.

O script usa apenas a biblioteca padrão para poder rodar localmente e no
GitHub Actions sem instalar dependências.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable


ROOT_REQUIRED = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "GOVERNANCE.md",
    "DATA_POLICY.md",
    "CITATION.cff",
    "docs/arquitetura.md",
    "templates/sisproj/projeto.md",
    ".github/pull_request_template.md",
)

PROJECT_REQUIRED = (
    "project.json",
    "README.md",
    "projeto.md",
    "cronograma.csv",
    "matriz-responsabilidades.md",
    "monitoramento-avaliacao.md",
    "governanca-lgpd.md",
    "checklist-sisproj.md",
)

PROJECT_HEADINGS = (
    "## 2. Resumo",
    "## 3. Problema e justificativa",
    "## 5. Objetivo geral",
    "## 6. Objetivos específicos",
    "## 8. Metodologia",
    "## 9. Fases de implantação",
    "## 12. Monitoramento e avaliação",
    "## 13. Ética, acessibilidade e proteção de dados",
    "## 18. Pendências para submissão",
)

CSV_FIELDS = (
    "eixo",
    "atividade",
    "descricao",
    "indicador_tipo",
    "indicador_fisico",
    "unidade",
    "meta",
    "data_inicio",
    "data_fim",
    "responsavel",
    "status",
    "evidencia",
)

FORBIDDEN_PARTS = {
    "dados-identificaveis",
    "dados-sensiveis",
    "private",
    "restricted",
}

FORBIDDEN_SUFFIXES = {
    ".docx",
    ".xlsx",
    ".xls",
    ".ods",
    ".sav",
    ".zsav",
    ".rdata",
    ".rds",
    ".sqlite",
    ".sqlite3",
    ".db",
    ".pem",
    ".key",
}

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
)

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".json",
    ".csv",
    ".yml",
    ".yaml",
    ".cff",
    ".toml",
}

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def parse_iso_date(raw: str, context: str, errors: list[str]) -> date | None:
    try:
        return date.fromisoformat(raw)
    except (TypeError, ValueError):
        errors.append(f"{context}: data inválida {raw!r}; use AAAA-MM-DD")
        return None


def read_json(path: Path, errors: list[str]) -> dict | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: JSON inválido: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path}: o conteúdo precisa ser um objeto JSON")
        return None
    return value


def validate_project_dir(project_dir: Path) -> list[str]:
    errors: list[str] = []

    for relative in PROJECT_REQUIRED:
        if not (project_dir / relative).is_file():
            errors.append(f"{project_dir}: arquivo obrigatório ausente: {relative}")

    metadata_path = project_dir / "project.json"
    schedule_path = project_dir / "cronograma.csv"
    proposal_path = project_dir / "projeto.md"
    if not metadata_path.is_file() or not schedule_path.is_file():
        return errors

    metadata = read_json(metadata_path, errors)
    if metadata is None:
        return errors

    required_keys = {
        "schema_version",
        "slug",
        "title",
        "status",
        "start_date",
        "end_date",
        "axes",
        "public_repository",
        "contains_personal_or_health_data",
    }
    missing_keys = sorted(required_keys - metadata.keys())
    if missing_keys:
        errors.append(f"{metadata_path}: chaves ausentes: {', '.join(missing_keys)}")

    slug = metadata.get("slug")
    if slug != project_dir.name:
        errors.append(
            f"{metadata_path}: slug {slug!r} deve coincidir com {project_dir.name!r}"
        )

    if metadata.get("public_repository") is not True:
        errors.append(f"{metadata_path}: public_repository deve ser true")
    if metadata.get("contains_personal_or_health_data") is not False:
        errors.append(
            f"{metadata_path}: repositório público não pode conter dados pessoais ou de saúde"
        )

    axes = metadata.get("axes")
    if not isinstance(axes, list) or not axes or not all(isinstance(x, str) and x for x in axes):
        errors.append(f"{metadata_path}: axes deve ser uma lista não vazia de textos")
        axes = []
    elif len(axes) != len(set(axes)):
        errors.append(f"{metadata_path}: axes contém valores duplicados")

    project_start = parse_iso_date(
        metadata.get("start_date"), f"{metadata_path}: start_date", errors
    )
    project_end = parse_iso_date(
        metadata.get("end_date"), f"{metadata_path}: end_date", errors
    )
    if project_start and project_end and project_start > project_end:
        errors.append(f"{metadata_path}: start_date deve ser anterior ou igual a end_date")

    rows: list[dict[str, str]] = []
    try:
        with schedule_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                errors.append(
                    f"{schedule_path}: cabeçalho deve ser exatamente {','.join(CSV_FIELDS)}"
                )
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{schedule_path}: CSV inválido: {exc}")
        return errors

    if not rows:
        errors.append(f"{schedule_path}: inclua ao menos uma atividade")
        return errors

    represented_axes: set[str] = set()
    starts: list[date] = []
    ends: list[date] = []
    for line_number, row in enumerate(rows, start=2):
        context = f"{schedule_path}:{line_number}"
        for field in CSV_FIELDS:
            if field != "evidencia" and not (row.get(field) or "").strip():
                errors.append(f"{context}: campo obrigatório vazio: {field}")

        axis = (row.get("eixo") or "").strip()
        if axis:
            represented_axes.add(axis)
            if axes and axis not in axes:
                errors.append(f"{context}: eixo {axis!r} não está em project.json")

        indicator_type = (row.get("indicador_tipo") or "").strip()
        if indicator_type not in {"quantitativo", "qualitativo"}:
            errors.append(
                f"{context}: indicador_tipo deve ser 'quantitativo' ou 'qualitativo'"
            )

        try:
            if Decimal((row.get("meta") or "").strip()) <= 0:
                raise InvalidOperation
        except (InvalidOperation, ValueError):
            errors.append(f"{context}: meta deve ser um número maior que zero")

        start = parse_iso_date(row.get("data_inicio"), f"{context}: data_inicio", errors)
        end = parse_iso_date(row.get("data_fim"), f"{context}: data_fim", errors)
        if start:
            starts.append(start)
        if end:
            ends.append(end)
        if start and end and start > end:
            errors.append(f"{context}: data_inicio deve ser anterior ou igual a data_fim")
        if project_start and start and start < project_start:
            errors.append(f"{context}: atividade começa antes da vigência")
        if project_end and end and end > project_end:
            errors.append(f"{context}: atividade termina depois da vigência")

    if axes:
        missing_axes = sorted(set(axes) - represented_axes)
        if missing_axes:
            errors.append(
                f"{schedule_path}: eixos sem atividade: {', '.join(missing_axes)}"
            )
    if project_start and starts and min(starts) != project_start:
        errors.append(
            f"{schedule_path}: ao menos uma atividade deve iniciar em {project_start.isoformat()}"
        )
    if project_end and ends and max(ends) != project_end:
        errors.append(
            f"{schedule_path}: ao menos uma atividade deve terminar em {project_end.isoformat()}"
        )

    if proposal_path.is_file():
        proposal = proposal_path.read_text(encoding="utf-8")
        for heading in PROJECT_HEADINGS:
            if heading not in proposal:
                errors.append(f"{proposal_path}: seção obrigatória ausente: {heading}")

    return errors


def iter_repository_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        yield path


def validate_public_files(root: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_repository_files(root):
        relative = path.relative_to(root)
        lowered_parts = {part.lower() for part in relative.parts}
        if lowered_parts & FORBIDDEN_PARTS:
            errors.append(f"{relative}: caminho reservado para conteúdo não público")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"{relative}: formato proibido no repositório público")
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE", ".gitignore"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"{relative}: arquivo textual não pôde ser lido como UTF-8")
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(f"{relative}: possível segredo ou chave privada detectado")
    return errors


def validate_relative_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(content):
            clean = target.strip().split()[0].strip("<>")
            if clean.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = clean.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(root)}: link sai do repositório: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: link relativo inexistente: {target}")
    return errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in ROOT_REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"arquivo obrigatório ausente: {relative}")

    projects_dir = root / "projects"
    if not projects_dir.is_dir():
        errors.append("diretório projects ausente")
    else:
        projects = sorted(path for path in projects_dir.iterdir() if path.is_dir())
        if not projects:
            errors.append("inclua ao menos um projeto em projects/")
        for project_dir in projects:
            errors.extend(validate_project_dir(project_dir))

    errors.extend(validate_public_files(root))
    errors.extend(validate_relative_links(root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="raiz do repositório",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate_repository(root)
    if errors:
        print(f"Falha de validação: {len(errors)} problema(s).", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    project_count = sum(1 for path in (root / "projects").iterdir() if path.is_dir())
    print(f"Validação concluída: {project_count} projeto(s), sem erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

