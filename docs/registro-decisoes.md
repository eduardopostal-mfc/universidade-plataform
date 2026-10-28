# Registro de decisões

## 2026-08-27 — Fundação do repositório

- **Decisão:** ampliar o repositório existente em vez de substituí-lo ou criar um fork integral.
- **Motivo:** nenhum template analisado cobre simultaneamente projeto universitário, educação, saúde, fluxo SisProj e proteção de dados brasileira.
- **Evidência:** comparação registrada em `docs/referencias-open-source.md`.
- **Consequência:** a arquitetura combina padrões compatíveis e mantém a licença MIT já existente.

## 2026-08-27 — GitHub como camada pública

- **Decisão:** proibir dados pessoais, dados de saúde e documentos administrativos restritos no repositório.
- **Motivo:** o caso de referência envolve saúde do trabalhador, neurodivergência e responsabilidades de cuidado; a publicação de dados brutos criaria risco desnecessário.
- **Consequência:** o repositório contém somente modelos, planos sanitizados e indicadores vazios ou agregados seguros.

## 2026-08-27 — Primeiro caso de referência

- **Decisão:** usar `Trabalho, Autismo e Cuidado na FURG` como primeiro projeto completo.
- **Motivo:** permite testar a estrutura com trilha de pares, formação de gestores, repositório educacional, governança e avaliação.
- **Questões abertas:** modalidade principal no SisProj, unidade gestora, coordenação formal, equipe, cargas horárias, anuências e datas definitivas.

## 2026-10-28 — Skills de Instagram no escopo do projeto

- **Decisão:** incorporar o pacote `instagram-agent-skill` (Jake Schincariol, MIT) em `.claude/skills/`, no escopo do projeto, em vez de instalar apenas na máquina de cada pessoa.
- **Motivo:** o guia "Skills de Instagram no Claude" (Deploy Club) recomenda a cópia das pastas `skills/ig-*` para `.claude/skills/` quando o uso é por projeto; versionar aqui mantém a mesma versão para toda a equipe e registra origem, commit e licença.
- **Evidência:** `.claude/skills/README.md` registra o commit de origem; `docs/skills-instagram-claude.md` adapta o guia em português.
- **Consequência:** o `voice.md` preenchido e qualquer dado de contas, comentários ou métricas ficam fora do repositório; o modelo versionado contém apenas campos vazios e a diretriz de idioma.

## 2026-10-28 — Skill `agencia` no repositório

- **Decisão:** incorporar apenas a skill `agencia` (orquestradora) em `.claude/skills/`, com seus dois modelos vazios, deixando as skills de papel que ela aciona fora do repositório por enquanto.
- **Motivo:** foi o pedido feito; a skill é de autoria própria e licença MIT, e os modelos não contêm dados.
- **Consequência:** `.claude/skills/README.md` lista as 15 dependências ausentes; a ficha preenchida, o calendário e as entregas de cada cliente permanecem fora do repositório.
