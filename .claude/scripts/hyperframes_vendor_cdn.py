#!/usr/bin/env python3
"""Troca bibliotecas do cdn.jsdelivr.net por cópias locais num projeto HyperFrames.

Os modelos do HyperFrames carregam scripts como o GSAP de
``https://cdn.jsdelivr.net/npm/<pacote>@<versão>/<arquivo>``. Quando a rede do
ambiente bloqueia esse domínio, a renderização falha. Este script baixa cada
pacote pelo registro do npm, copia o arquivo para ``assets/vendor/`` e reescreve
os HTML do projeto para usar a cópia local.

Uso: python3 .claude/scripts/hyperframes_vendor_cdn.py <pasta-do-projeto>
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path


CDN_PATTERN = re.compile(
    r"https://cdn\.jsdelivr\.net/npm/"
    r"(?P<package>(?:@[A-Za-z0-9._-]+/)?[A-Za-z0-9._-]+)"
    r"@(?P<version>[A-Za-z0-9.^~<>=*_-]+)"
    r"/(?P<file>[^\"'\s)?#]+)"
)


def fetch_package(spec: str, workdir: Path) -> Path:
    """Baixa o pacote com ``npm pack`` e devolve a pasta extraída."""
    target = workdir / re.sub(r"[^A-Za-z0-9._-]", "_", spec)
    target.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["npm", "pack", spec, "--silent", "--pack-destination", str(target)],
        capture_output=True,
        text=True,
        check=True,
    )
    tarball = target / result.stdout.strip().splitlines()[-1]
    with tarfile.open(tarball) as archive:
        archive.extractall(target, filter="data")
    return target / "package"


def vendor_project(project: Path) -> int:
    html_files = [p for p in project.rglob("*.html") if "node_modules" not in p.parts]
    urls = sorted(
        {m.group(0) for p in html_files for m in CDN_PATTERN.finditer(p.read_text(encoding="utf-8"))}
    )
    if not urls:
        print("Nenhuma biblioteca do cdn.jsdelivr.net encontrada.")
        return 0

    replacements: dict[str, str] = {}
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        packages: dict[str, Path] = {}
        for url in urls:
            match = CDN_PATTERN.fullmatch(url)
            package, version, file = match["package"], match["version"], match["file"]
            spec = f"{package}@{version}"
            try:
                if spec not in packages:
                    packages[spec] = fetch_package(spec, Path(tmp))
            except subprocess.CalledProcessError as exc:
                print(f"ERRO: npm pack {spec} falhou: {exc.stderr.strip()}", file=sys.stderr)
                failures += 1
                continue
            source = packages[spec] / file
            if not source.is_file():
                print(f"ERRO: {file} não existe no pacote {spec}", file=sys.stderr)
                failures += 1
                continue
            local = Path("assets/vendor") / spec / file
            (project / local).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, project / local)
            replacements[url] = local.as_posix()
            print(f"{url} -> {local.as_posix()}")

    # Caminhos relativos à raiz do projeto, como o HyperFrames exige também
    # nas subcomposições.
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        updated = text
        for url, local in replacements.items():
            updated = updated.replace(url, local)
        if updated != text:
            path.write_text(updated, encoding="utf-8")

    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("project", type=Path, help="pasta do projeto HyperFrames")
    args = parser.parse_args()
    if not (args.project / "index.html").is_file():
        parser.error(f"{args.project} não parece um projeto HyperFrames (sem index.html)")
    return vendor_project(args.project.resolve())


if __name__ == "__main__":
    sys.exit(main())
