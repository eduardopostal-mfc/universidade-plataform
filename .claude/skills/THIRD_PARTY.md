# Skills de terceiros

Skills de vídeo com IA copiadas sem alterações dos repositórios abaixo, para
uso com o Claude Code neste projeto. As licenças originais estão em
`licenses/`.

| Skills | Origem | Commit | Licença |
|---|---|---|---|
| `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `figma`, `slideshow`, `remotion-to-hyperframes` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) (`skills/`) | `807803a` | Apache-2.0 |
| `heygen-avatar`, `heygen-video`, `heygen-translate` | [heygen-com/skills](https://github.com/heygen-com/skills) | `1bd5e4d` | MIT |
| `runway-dev`, `runway-dev-setup`, `runway-dev-models`, `runway-dev-model-routers`, `runway-dev-characters`, `runway-dev-recipes`, `runway-dev-workflows` | [runwayml/skills](https://github.com/runwayml/skills) (`skills/`) | `3dcbb5b` | MIT |
| `runway-ml` | [TerminalSkills/skills](https://github.com/TerminalSkills/skills) (`skills/runway-ml/`, sem `_scores.json`) | `20719c3` | Apache-2.0 |

## Requisitos de uso

- **HyperFrames:** Node.js 22+ e FFmpeg. A CLI roda via `npx hyperframes`.
- **HeyGen:** conector MCP da HeyGen (`https://mcp.heygen.com/mcp/v1/`, usa os
  créditos do plano) ou a CLI `heygen` com `HEYGEN_API_KEY` (cobrada como API).
- **Runway:** conta no Runway Developer Portal e `RUNWAYML_API_SECRET`, com
  créditos pré-pagos. Nunca coloque a chave no código nem no repositório.

## Atualizar

Clone o repositório de origem, substitua a pasta da skill pela versão nova e
atualize o commit nesta tabela.
