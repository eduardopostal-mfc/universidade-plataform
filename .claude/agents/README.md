# Agentes da agência de conteúdo

Agentes do Claude Code (subagentes) que transformam a skill `agencia` em um **agente coordenador** com um time de especialistas. Cada arquivo `.md` desta pasta define um agente; o Claude Code os carrega ao abrir este repositório.

## Como usar

No Claude Code, dentro deste repositório, peça em linguagem natural ("planeja minha semana no Instagram", "produz um carrossel sobre X") ou nomeie o agente: "use o agente agencia para montar a pauta da semana". O coordenador escolhe o fluxo, delega cada papel a um subagente e devolve só o que passou no controle de qualidade.

Para um pedido de um papel só ("uma legenda para esse reel"), o agente daquele papel pode ser chamado diretamente.

## O time

| Agente | Papel | Skill que carrega |
|---|---|---|
| `agencia` | Coordenação: ficha, fluxo, delegação, QC, fechamento | `agencia` |
| `estrategia` | Estrategista | `estrategia` |
| `espionagem` | Pesquisa | `espionagem` |
| `marca` | Marca pessoal | `marca` |
| `roteiro` | Roteirista | `roteiro` |
| `direcao-criativa` | Direção criativa | `direcao-criativa` |
| `stories` | Stories e direct | `stories` |
| `analise` | Análise | `analise` |
| `reel` | Reel tipográfico | `reel` |
| `editor-video` | Editor de vídeo | `editor-video` |
| `carrossel` | Design de carrossel | `carrossel` |
| `legenda` | Copy de legenda | `legenda` |
| `perfil` | Perfil e bio | `perfil` |
| `comentarios` | Comunidade | `comentarios` |
| `design-marketing-medico` | Design e compliance médico | `design-marketing-medico` |
| `revisor-mini-di` | Revisão Mini Di (FVC e checklist) | `efeito-di` |

## Regras fixas

- Cada subagente começa sem contexto: o coordenador cola a ficha, a entrada do passo e a pasta de entrega no prompt (contrato de delegação em `agencia.md`).
- Nenhum agente publica, comenta, segue ou manda DM. Tudo termina em texto e arquivos para a pessoa aprovar.
- A ficha preenchida, o calendário e as entregas de cada cliente ficam na pasta de trabalho do cliente, fora deste repositório público.
