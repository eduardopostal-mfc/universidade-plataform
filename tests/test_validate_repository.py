from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import CSV_FIELDS, validate_project_dir


class ProjectValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_dir = Path(self.temp_dir.name) / "example"
        self.project_dir.mkdir()
        for name in (
            "README.md",
            "matriz-responsabilidades.md",
            "monitoramento-avaliacao.md",
            "governanca-lgpd.md",
            "checklist-sisproj.md",
        ):
            (self.project_dir / name).write_text("# Documento\n", encoding="utf-8")

        proposal = "# Projeto\n\n" + "\n\n".join(
            f"{heading}\n\nConteúdo." for heading in (
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
        )
        (self.project_dir / "projeto.md").write_text(proposal, encoding="utf-8")

        metadata = {
            "schema_version": 1,
            "slug": "example",
            "title": "Example",
            "status": "draft",
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "axes": ["planning", "evaluation"],
            "public_repository": True,
            "contains_personal_or_health_data": False,
        }
        (self.project_dir / "project.json").write_text(
            json.dumps(metadata), encoding="utf-8"
        )
        self.write_schedule(
            [
                self.row("planning", "Plan", "2026-01-01", "2026-06-30"),
                self.row("evaluation", "Evaluate", "2026-07-01", "2026-12-31"),
            ]
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    @staticmethod
    def row(axis: str, activity: str, start: str, end: str) -> dict[str, str]:
        return {
            "eixo": axis,
            "atividade": activity,
            "descricao": "Description",
            "indicador_tipo": "quantitativo",
            "indicador_fisico": "Output",
            "unidade": "unit",
            "meta": "1",
            "data_inicio": start,
            "data_fim": end,
            "responsavel": "Coordinator",
            "status": "planned",
            "evidencia": "",
        }

    def write_schedule(self, rows: list[dict[str, str]]) -> None:
        with (self.project_dir / "cronograma.csv").open(
            "w", encoding="utf-8", newline=""
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def test_valid_project(self) -> None:
        self.assertEqual(validate_project_dir(self.project_dir), [])

    def test_rejects_missing_axis_and_out_of_range_date(self) -> None:
        self.write_schedule(
            [self.row("planning", "Plan", "2025-12-31", "2026-12-31")]
        )
        errors = validate_project_dir(self.project_dir)
        joined = "\n".join(errors)
        self.assertIn("eixos sem atividade: evaluation", joined)
        self.assertIn("atividade começa antes da vigência", joined)

    def test_rejects_sensitive_data_flag(self) -> None:
        path = self.project_dir / "project.json"
        metadata = json.loads(path.read_text(encoding="utf-8"))
        metadata["contains_personal_or_health_data"] = True
        path.write_text(json.dumps(metadata), encoding="utf-8")
        errors = validate_project_dir(self.project_dir)
        self.assertTrue(any("dados pessoais ou de saúde" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

