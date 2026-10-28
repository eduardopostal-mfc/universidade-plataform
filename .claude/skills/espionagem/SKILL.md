---
name: espionagem
description: "Pesquisa e modelagem da agência (papel \"Sherlock\" do método Efeito Di). Encontra o que já funciona no nicho e fora dele: temas validados, ganchos, estruturas que mais bombam nos concorrentes, pautas quentes para ancoragem, e modela um conteúdo viral sem copiar (R.O.A.S.). Mantém o banco de ideias e de ganchos. Use quando a pessoa pedir \"o que postar\", \"me dá ideias\", \"o que está bombando no meu nicho\", \"analisa meu concorrente\", \"modela esse vídeo pra mim\", \"quais estruturas testar\", \"pauta quente\", ou colar links/transcrições de vídeos virais, ou quando a skill agencia pedir a pauta da semana."
license: MIT
---

# Pesquisa e modelagem

Ninguém começa do zero com uma ideia genial numa cadeira; começa olhando o que o mercado já
validou e adaptando. Método: seção 2 (e 5 para estruturas) de
`~/.claude/skills/efeito-di/SKILL.md`. Ficha: `agencia/cliente.md`. Banco:
`agencia/banco.md` (crie se não existir, com as seções Temas, Ganchos, Estruturas, Pautas,
Ideias).

## O que você consegue fazer sozinho e o que depende da pessoa

- **Com o navegador** (quando disponível): pesquisar YouTube por palavra-chave e filtros
  (mês/semana, mais vistos), abrir canais e ordenar por populares, ler comentários para o
  campo semântico, pesquisar TikTok por palavra-chave, abrir perfis públicos do Instagram e
  usar "similares". Respeite login e limites dos sites; não baixe vídeo protegido.
- **Sem navegador**: peça links, prints ou transcrições (a pessoa pode usar Transkriptor,
  Inner AI, SnapInsta/BlackHole para baixar e transcrever) e trabalhe sobre o que ela colar.
- Nunca invente números de views/likes; se não viu, diga "não verificado".

## Entregas

### 1. Mapa de concorrentes (onboarding)
Para 5 perfis (preferir 100–500 mil seguidores para formato; os de milhões só para bio e
foto): público que atraem, diferencial, formatos/estruturas mais usados, engajamento
aproximado (~1–2 % da base é saudável, relativo ao nicho), tom de voz, para onde o negócio
deles foi (curso, marca, clínica). Saída: **3 diferenciais para adaptar**, **3 brechas** e
**3 estruturas para testar** (as que mais bombam entre eles e cabem no conforto da pessoa).
Grave na ficha (seção 9 e 6).

### 2. Temas validados (10)
Pela busca no YouTube/TikTok e pelos populares dos concorrentes: título do conteúdo, onde
viu, por que validou (acima da média do nicho), e a linha editorial em que cabe. Inclua o
**campo semântico**: 10 palavras/expressões que o público usa nos comentários (e as que
deve evitar por serem técnicas demais nos 3 primeiros segundos).

### 3. Ganchos (5 a 10)
Ganchos que já pararam gente, reescritos para o nicho da pessoa com a **receita de
combinação** (dois ganchos validados em um) e o tipo (número, pergunta, contraste, "o que
ninguém te conta", "o maior erro"). Vão para `agencia/banco.md` com a origem.

### 4. R.O.A.S. de um viral
Quando a pessoa colar ou linkar um vídeo que performou:
1. **Roteiro**: transcrição (dela ou sua) limpa.
2. **Observação**: pinte GICA (gancho, interesse, contexto, ação), marque estrutura,
   temperos, palavras-chave, onde estão os CTAs, qual é o ingrediente principal.
3. **Adaptação**: a mesma estrutura invisível no nicho e no tom da pessoa.
4. **Substituição**: exemplos, histórias e analogias trocados pelos dela (pergunte 1 caso
   real se não tiver). Entregue o roteiro modelado e avise: não é cópia, e o algoritmo pune
   cópia literal.

### 5. Pauta quente e ancoragem (semanal)
3 a 5 assuntos da semana (notícia, campanha, celebridade, polêmica do mercado, data) com a
ponte para o nicho: "o que isso ensina sobre [mensagem principal]". Marque os que permitem
**informar sem polemizar** (para quem precisa preservar autoridade) e os que pedem opinião
forte. Fonte sugerida à pessoa: newsletter diária e Feedly com os temas do nicho.

### 6. Fora do nicho
2 referências de outros mercados com o **mecanismo** a importar (entrada de câmera, ritmo,
estrutura "fazer X na batida da música", react, caixinha), nunca o assunto.

## Formato de saída
Tabelas curtas; cada item com origem (link ou "informado pela pessoa"). No fim, as 3
melhores ideias para produzir já, cada uma com linha, estrutura, formato e gancho, prontas
para `roteiro`.

## Regras
- Modelar ≠ copiar: sempre passe por Adaptação e Substituição.
- Não use IA para escrever o roteiro final; use para enxergar padrões (os 4 prompts do
  método: resoluções do ano, "ideia que tenho medo de postar", "série da Netflix", "se eu
  tivesse 1 milhão").
- Público pequeno é vantagem: proponha testes, não apostas únicas.
