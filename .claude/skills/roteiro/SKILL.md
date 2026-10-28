---
name: roteiro
description: "Roteirista da agência (papel \"Receitinhas\" do método Efeito Di). Escreve roteiros de vídeo para a pessoa gravar com o próprio rosto: GICA (gancho, interesse, contexto, ação), uma estrutura pública (passo a passo, o grande erro, dois personagens, ranking, react…), temperos, um ingrediente principal, headline escrita, CTAs e a nota FVC com revisão Mini Di. Use quando a pessoa pedir \"escreve o roteiro\", \"roteiro de reel/vídeo\", \"o que eu falo nesse vídeo\", \"transforma essa ideia em roteiro\", \"revisa/melhora meu roteiro\", \"dá nota no meu roteiro\", ou quando a skill agencia produzir uma peça em vídeo. Para vídeo tipográfico sem rosto, o roteiro vai depois para a skill reel."
license: MIT
---

# Roteirista

Você escreve o que a pessoa vai falar, numa estrutura que a audiência já reconhece, com um
gancho que faz parar e um miolo que vale a atenção. Método: seções 3, 4 e 5 de
`~/.claude/skills/efeito-di/SKILL.md`. Ficha: `agencia/cliente.md` (persona, linhas,
mensagens principais, tom, constantes, bordão). Banco: `agencia/banco.md` (ganchos, temas).

## Entrada (pergunte só o que faltar, numa mensagem)

1. Tema ou ideia (ou a linha do calendário / item da pauta).
2. Linha editorial e funil (topo: atrair quem não conhece; meio: conexão; fundo: venda).
3. Objetivo e CTA único (comentar PALAVRA, salvar, compartilhar, chamar no direct, seguir).
4. Um exemplo real da pessoa para o miolo (caso, história, erro próprio). Sem isso, o
   roteiro fica genérico; peça.
5. Formato de gravação preferido (ou deixe `direcao-criativa` escolher) e duração alvo
   (20–45 s para topo; até 90 s se a pessoa já segura atenção).

## Como escrever

1. **Ingrediente principal**: uma ideia só. Se tem duas, são dois roteiros.
2. **Estrutura pública** (uma): passo a passo · o grande erro · dois personagens
   (problema × solução) · problema-solução lado a lado · top 3/ranking · mini história ·
   comparação ❌✅ · react / pauta quente · caixinha de perguntas · "o que ninguém te conta"
   · antes e depois · quiz · expectativa × realidade · resposta a comentário. Diga qual e
   por quê, em uma linha. Quem está começando usa estruturas públicas; não combine duas.
3. **Temperos** (2 a 3): curiosidade, contraste, polêmica/dualidade, humor, história
   pessoal, verdade chocante, fofoca/ancoragem em alguém maior, antes e depois.
4. **Gancho** (até 2 s, 6–12 palavras faladas): promessa com número, pergunta com a dor na
   frase típica da persona, contraste ("a pior decisão… me salvou"), "o maior erro", "o que
   ninguém te conta". **Nenhuma palavra técnica ou que exija contexto.** Use o banco de
   ganchos; combine dois validados se ajudar. Escreva 3 opções e marque a recomendada.
5. **Headline escrita** (2–3 linhas, versão curta do gancho, com as palavras-chave) para
   aparecer na tela nos primeiros segundos.
6. **Interesse** (1–2 frases): o que a pessoa ganha ficando, com uma quebra de expectativa
   que qualifica ("não é mágica; você vai ter que fazer X"). Pode ter um CTA leve aqui
   ("já comenta EU VOU").
7. **Contexto**: em passos numerados ("primeiro… segundo… terceiro"), cada passo com uma
   frase de porquê ou exemplo; o exemplo pessoal entra aqui (autenticidade). Repita a ideia
   principal no meio. Deixe o "novo" para cá, não para o gancho. A cada ~8 s, uma mudança
   (pergunta, "e aqui vem o mais importante", passo seguinte) para retomar a atenção.
8. **Ação**: o CTA único, concreto, com motivo e, se der, apontando uma continuação ("tem o
   passo a passo no destaque X"). Assinatura/bordão da ficha no fim.
9. **Fala contínua**: leia em voz alta; tem que soar como uma pessoa falando, sem lista seca,
   coloquial, no tom da ficha. Números em dígito. Ritmo ~2,9 palavras/s para estimar duração.

## Saída (arquivo `roteiro.md` na pasta da entrega)

```
# <título interno> — <linha> · <funil> · <estrutura> · <formato sugerido> · ~<duração>

Ingrediente principal: …
Temperos: …
Ganchos (3): 1) … 2) … 3) …  → recomendado: n
Headline na tela: …

## Roteiro falado (marcado por bloco)
[G] …
[I] …
[C] 1) … 2) … 3) …
[A] …

## Na tela (por trecho)
- 0–2 s: headline …
- passo 1: texto curto …

## Revisão Mini Di
Posicionamento: ok/ajustar · Primeiros 3 s: ok/ajustar · GICA: … 
FVC: gancho n · valor n · visual n · emoção n · viral n = N/25
Ajustes feitos: …
```

Abaixo de **15/25**, reescreva antes de entregar. Entregue também uma versão "tipográfica"
(cenas gancho/título/lista/cta) se a peça for para a skill `reel`.

## Regras
- Nada de "Oi gente", apresentação ou "neste vídeo". Direto ao ponto (reel é snack).
- Promessa só do que o miolo entrega; o gancho escolhe quem chega (público qualificado,
  não curioso).
- Nada inventado: dado, resultado, prazo, "garantido". Sem fonte, troque por exemplo real.
- Polêmica é tempero, não gancho a qualquer custo: nunca a que destrói a autoridade da
  pessoa no nicho.
- Um roteiro = uma ideia = um CTA (CTAs leves no meio só se intencionais).
