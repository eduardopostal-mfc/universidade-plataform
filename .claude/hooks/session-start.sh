#!/bin/bash
# Prepara o HyperFrames nas sessões de nuvem do Claude Code.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# O HyperFrames procura o Chrome Headless Shell e tentaria baixá-lo; o
# ambiente de nuvem já traz um, instalado pelo Playwright.
browser=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell 2>/dev/null | sort -V | tail -n 1 || true)
if [ -n "$browser" ] && [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export HYPERFRAMES_BROWSER_PATH=\"$browser\"" >> "$CLAUDE_ENV_FILE"
fi

# As skills ficam fixadas em .claude/skills (ver THIRD_PARTY.md); o
# `hyperframes init` não deve instalar outras versões por cima.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export HYPERFRAMES_SKIP_SKILLS=1" >> "$CLAUDE_ENV_FILE"
fi

# Os modelos do HyperFrames carregam o GSAP e outras bibliotecas do
# cdn.jsdelivr.net. Se a rede bloquear o domínio, o aviso abaixo entra no
# contexto da sessão.
if ! curl -sS -o /dev/null --max-time 5 https://cdn.jsdelivr.net/npm/gsap@3.14.2/package.json 2>/dev/null; then
  echo "cdn.jsdelivr.net está bloqueado neste ambiente. Antes de renderizar ou pré-visualizar um projeto HyperFrames, rode: python3 \"${CLAUDE_PROJECT_DIR:-.}/.claude/scripts/hyperframes_vendor_cdn.py\" <pasta-do-projeto>"
fi
