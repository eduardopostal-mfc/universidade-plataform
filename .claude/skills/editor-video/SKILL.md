---
name: editor-video
description: "Editor de vídeo da agência (método Efeito Di). Transforma vídeo já gravado (bruto do celular, reel antigo, aula, live) em reel 1080x1920 pronto, no computador da pessoa: inventaria e transcreve com tempo, escolhe os cortes (gancho nos 3 s, sem cumprimento, 45–65 s), monta no estúdio Remotion com headline, selo do quadro, legenda automática em caixa (palavra a palavra via Whisper), textos blocados, rodapé de identificação e cartão final de CTA, e renderiza o MP4 (versão final e versão leve para o Drive). Use quando a pessoa pedir \"edita esse vídeo\", \"corta esse vídeo em reel\", \"monta um reel com o que eu já gravei\", \"põe legenda/rodapé/CRM nesse vídeo\", \"transcreve esse vídeo\", \"o que dá pra aproveitar das minhas gravações\", ou quando a skill agencia produzir uma peça a partir de vídeo gravado. Não grava nada: o roteiro é da skill roteiro e a gravação é da pessoa (direcao-criativa)."
license: MIT
---

# Editor de vídeo: do bruto ao reel pronto

Você recebe um vídeo que já existe (bruto do celular, reel editado antigo, aula) e devolve um reel
vertical pronto para postar, montado no **estúdio de reels** (`~/reels-estudio`, o mesmo da skill
`reel`) pela composição **Gravado**. Nada sai para app de edição; tudo roda no computador da pessoa.

`<skill>` é a pasta desta skill. Método: `~/.claude/skills/efeito-di/SKILL.md` (seções 4, 5 e 6).
Ficha do cliente: `agencia/cliente.md` (constantes de marca, identificação, palavra-chave, ética).

## Pré-requisitos (uma vez)
- Estúdio da skill `reel` instalado em `~/reels-estudio` com `src/Gravado.tsx` e a composição
  `Gravado` registrada em `src/Root.tsx` (cópias em `<skill>/estudio/`; se faltarem, copie e rode
  `npx tsc --noEmit`). Node fica em `~/reels-estudio/.node/bin` nesta máquina.
- Whisper: `~/reels-estudio/.venv` (python 3.9+ com `faster-whisper` e `pillow`). Se não existir:
  `python3 -m venv ~/reels-estudio/.venv && ~/reels-estudio/.venv/bin/pip install faster-whisper pillow`.
  O modelo `small` baixa no primeiro uso (~460 MB).
- `probe`: `swiftc -O <skill>/scripts/probe.swift -o ~/reels-estudio/.bin/probe` (macOS; AVFoundation).
  Dá duração, dimensões, fps, faixas de áudio, exporta o áudio `.m4a` e 3 quadros `.jpg` por vídeo.

## O fluxo, em 8 passos

### 1. Inventário
```
~/reels-estudio/.bin/probe <pasta-de-saída> video1.mov video2.mov …
```
Monte uma folha com os quadros (3 por vídeo) e olhe: cenário, enquadramento, se já tem legenda
queimada, cartão/cabeçalho próprio, se está **espelhado** (texto ao contrário) ou escuro. Anote
em `inventario.md`: arquivo, duração, estado (bruto/editado), tema, linha editorial, o que falta.

### 2. Transcrição com tempo
```
~/reels-estudio/.venv/bin/python -I <skill>/scripts/transcrever.py <saída> a.m4a b.m4a   # [t0–t1] texto
~/reels-estudio/.venv/bin/python -I <skill>/scripts/palavras.py a.m4a a.palavras.json       # só se o vídeo precisar de legenda
```
Rode em background (`nohup … &`) e siga; ~1 min por 5 min de áudio no modelo small. A transcrição
automática erra nomes próprios e termos técnicos: marque para a pessoa validar antes de postar.

### 3. Escolha dos cortes (o roteiro invisível)
Leia a transcrição como roteiro e escolha trechos que formem **GICA**:
- **Gancho nos 3 primeiros segundos**: comece numa frase forte (contraste, número, pergunta com a
  dor). Corte cumprimentos ("Olá, meu nome é…"), "neste vídeo", pigarro, pausa longa.
- Se o vídeo original abre com uma cartela própria que já funciona como gancho, deixe-a fazer o
  trabalho e **não** ponha headline em cima (ela só confunde).
- **Interesse** logo depois (promessa do que vem), **contexto** em 2–4 blocos (mantenha "primeiro,
  segundo, terceiro" quando existir), **ação** no cartão final.
- Alvo **45–65 s** (até 90 s se for conexão/história que segura). Tire o que é técnico demais para
  a língua do público (estatística, nomes de teorias, listas longas) — vai para a legenda ou para
  um material (guia).
- Corte em fronteiras de frase; deixe 0,1–0,2 s de folga; evite colar duas frases que começam com
  a mesma palavra.
- Pontos que a pessoa precisa validar (clínico, nomes, datas) ficam listados no `roteiro-e-legenda.md`.

### 4. `gravado.json` (uma pasta por reel em `~/reels-estudio/reels/<slug>/`)
Coloque o vídeo em `reels/<slug>/public/fonte.mov` por **cópia ou hard link** (`ln`); symlink para
fora do estúdio dá 404 no render. Exemplo completo em `<skill>/estudio/exemplo-gravado.json`.

| Campo | O que é |
|---|---|
| `video` | arquivo em `public/` |
| `cortes` | `[{inicio, fim}]` em segundos do original, na ordem final |
| `headline` | `{texto, destaque?, duracao (2,5–3 s), topo (px; 170 por padrão, ~1120 se o rosto ocupa o topo), tamanho}` — caixa pêssego, Oswald caixa-alta; `null` se o vídeo já tem cartela de gancho |
| `selo` | texto do quadro ("Cuidado afirmativo"); `null` se o vídeo já tem cabeçalho próprio |
| `legenda` | blocos `[{inicio, fim, texto}]` no tempo final, gerados por `legenda-blocos.py` — só para vídeo **sem** legenda queimada |
| `textos` | textos blocados em momentos marcados (`{inicio, fim, texto, topo}`): contrapeso, dado, aviso |
| `rodape` | identificação fixa na base (para médico: `Nome · MÉDICO · CRM-UF n · Especialidade · RQE n`) |
| `fechamento` | cartão final: `{duracao (4,5–5 s), chamada, palavra, promessa, assinatura{marca, descricao, whatsapp, detalhe, nome, registro, perfil}}` |
| `espelhar` | `true` desespelha vídeo gravado com texto ao contrário |
| `filtro` | CSS, ex. `"brightness(1.18) contrast(1.04)"` para bruto contra a luz |
| `cores`, `fonte`, `fonteItalica`, `volume` | como na skill `reel` (paleta e fontes da ficha) |

Legenda automática:
```
~/reels-estudio/.venv/bin/python -I <skill>/scripts/legenda-blocos.py a.palavras.json "26.1-42.8,56.5-67.5" 4 > blocos.json
```
e cole o resultado em `legenda`. Blocos de até 4 palavras ou até a pontuação; revise o texto.

### 5. Quadros de conferência
```
cd ~/reels-estudio && npx remotion still Gravado out/<slug>-q30.png --props=reels/<slug>/gravado.json --public-dir=reels/<slug>/public --frame=30
```
Faça 3–4: gancho/headline (frame 30), meio (um bloco de legenda e um texto blocado), e o cartão
(últimos 30 frames). Olhe numa folha única. Conserte sobreposições (headline em cima do rosto ou de
cartela do vídeo, legenda em cima de legenda queimada) antes de renderizar.

### 6. Render
```
npx remotion render Gravado out/<slug>.mp4 --props=reels/<slug>/gravado.json --public-dir=reels/<slug>/public --crf 24          # final (postar)
npx remotion render Gravado out/<slug>-leve.mp4 --props=… --public-dir=… --crf 34   # leve ≤ 10 MB para subir no Drive (crf 37 se passar)
```
`--crf` e `--video-bitrate` não podem ir juntos (o estúdio já fixa crf no config). Renders longos em
background, um de cada vez. Vídeo de 60 s com rosto fica entre 25 e 55 MB no final.

### 7. Legenda e QC
`legenda` → 3 primeiras linhas, legenda completa, CTA único igual ao cartão, rodapé de
identificação e aviso quando for saúde. Revisão **Mini Di** (FVC) + ética da ficha (seção 11 quando
existir): sem diagnóstico ao espectador, sem antes-e-depois, sem paciente, sem promessa;
contrapeso para intervalos/listas ("depende da sua avaliação"). Liste o que a pessoa valida.

### 8. Entrega
`agencia/entregas/<AAAA-MM-DD>-<slug>/` com `gravado.json`, `roteiro-e-legenda.md` (cortes em
tabela, sobreposições, o que ficou de fora e por quê, legenda, QC) e `out/` (MP4 final, leve e os
quadros). Anote na ficha (seção 10) e no calendário. No Drive: docs pela ferramenta do Drive; MP4 leve
pelo Chrome (limite de 10 MB por envio); o final em alta fica local até a pessoa pedir.

## Decisões rápidas
| Situação | Faça |
|---|---|
| Vídeo já legendado (caixas queimadas) | `legenda: null`; só headline (ou nenhuma), rodapé e cartão |
| Vídeo com cabeçalho/cartela própria | `selo: null`; headline mais baixa ou nenhuma |
| Texto ao contrário nos quadros | `espelhar: true` |
| Contra a luz / escuro | `filtro: "brightness(1.15) contrast(1.05)"` |
| Fala com intervalo/dose/lista fechada | texto blocado de contrapeso + frase na legenda |
| Blooper/piada que fere a imagem profissional (ex.: cigarro) | fora do corte, sempre |
| Vídeo > 90 s mesmo cortado | dois reels (parte 1 e 2) com gancho próprio cada |

## Regras
- Nunca invente fala: só o que está na transcrição; a pessoa valida nomes, datas e dados.
- Rosto e voz reais são o padrão; sem clone, sem dublagem sintética.
- Identificação profissional em toda peça que circula sozinha (rodapé + cartão), quando a ficha exigir.
- Modelar ≠ copiar: o corte segue a estrutura GICA, não o estilo de outro perfil.
- Sem escassez ou urgência falsas no cartão; CTA único e coerente com a legenda.
