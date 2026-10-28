# Skills de Instagram no Claude

Guia operacional das 13 skills `/ig-*` incorporadas em [`.claude/skills/`](../.claude/skills/README.md). O texto adapta, em português, o guia "Skills de Instagram no Claude" da Deploy Club (Vinícius Guimarães, outubro de 2026), que por sua vez traduz o guia do autor do pacote, Jake Schincariol (licença MIT). Nenhum dos dois é afiliado ao Instagram.

## Como funciona

1. **Instalar** o pacote (feito neste repositório: as pastas estão em `.claude/skills/ig-*`).
2. **Configurar a voz** em um arquivo `voice.md` que todas as skills leem.
3. **Rodar as skills**: post, comentário, perfil, semana e viralidade.
4. **Aprovar e postar.** As skills escrevem; quem aperta "publicar" é a pessoa.

As skills não postam, não comentam, não seguem e não mandam DM por conta própria. Automação desse tipo, por robô no navegador ou ferramenta de terceiro, viola os Termos de Uso do Instagram e leva a bloqueio. Tudo aqui termina em texto pronto para copiar. A única exceção é a resposta automática por palavra-chave no direct, que o Instagram permite pelas ferramentas dele e de parceiros aprovados.

## Instalação

Neste repositório as skills já estão instaladas no escopo do projeto. Para usar em qualquer projeto ou globalmente:

```bash
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
```

Como plugin no Claude Code:

```
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent
```

No claude.ai ou no app, sem Claude Code: compacte a pasta de uma skill (por exemplo `skills/ig-viral`) e envie em Personalizar > Skills, com "Execução de código e criação de arquivos" ligada. Também dá para colar um `SKILL.md` no começo do chat; a skill funciona como um modo, mas sem as 5 ferramentas em Python, que são a parte que mais pesa em `/ig-reel` e `/ig-human`.

## O seu perfil de voz

Dez minutos aqui são o que faz cada post sair com o seu jeito e não com cara de IA. Todas as skills leem um arquivo só: `~/.claude/instagram/voice.md`.

- **Na mão:** copie o modelo [`.claude/instagram/voice.md`](../.claude/instagram/voice.md) para `~/.claude/instagram/voice.md` e preencha.
- **Deixando o Claude escrever:** cole a transcrição ou a legenda de 3 dos seus melhores reels e mande:

```
Aqui tão 3 reels meus. Escreve o meu voice.md a partir deles: o meu tom, o tamanho
das minhas frases, as palavras que eu sempre uso, as que eu nunca uso e com quem eu
tô falando. Salva como o meu perfil de voz do Instagram.

[cola aqui a transcrição ou a legenda dos 3 reels]
```

As skills foram escritas em inglês. O modelo deste repositório já traz a linha "escreve sempre em português do Brasil". A lista de palavras "de IA" que o humanizador remove é em inglês, então em português a revisão final é sua.

O `voice.md` preenchido fica fora do repositório: ele contém nome, handle, posições pessoais e números que não devem ser publicados aqui.

## O que cada skill faz

| Comando | O que faz |
| --- | --- |
| `/ig-reel` | Uma ideia vira um reel: 3 ganchos tirados de 26 fórmulas, com nota, o roteiro, o texto na tela e o tempo de cada trecho. |
| `/ig-viral` | A de viralidade. Acha o que está funcionando no seu nicho, ranqueia pelo quanto cada post passou da média da própria conta, diz a fórmula e monta o seu arquivo de referências. |
| `/ig-caption` | A legenda, revisada, mostrando os 125 caracteres que o feed exibe antes do "mais". |
| `/ig-carousel` | Carrossel: a capa que faz deslizar, o texto de cada slide e os arquivos em 1080x1350. |
| `/ig-story` | A sequência de Stories do dia, qual figurinha faz o quê e o funil para o direct. |
| `/ig-profile` | Dá nota de 0 a 100 para o seu perfil em 12 critérios e reescreve começando pelo que mais custa seguidor. |
| `/ig-plan` | A semana: o que postar, em que formato, quando e as 10 contas para interagir. |
| `/ig-human` | O humanizador: tira palavra com cara de IA e caractere invisível, e dá nota para o texto. |
| `/ig-comment` | Comentário no post dos outros: 9 tipos, escolhidos pelo que o post é. |
| `/ig-reply` | As respostas no seu post: separa em palavra-chave, lead, pergunta, apoio e ruído, e responde nessa ordem. |
| `/ig-dm` | O direct da palavra-chave, a primeira mensagem, a proposta de parceria e dois follow-ups. |
| `/ig-repurpose` | Um vídeo, podcast ou newsletter vira uma semana de reels e carrosséis. |
| `/ig-audit` | Raio-x do que você já postou, ranqueado pelo quanto passou da sua média. |

No Claude Code você chama pelo comando. No claude.ai, pelo nome da skill no pedido ("usa a ig-viral pra...").

## A skill de viralidade

Ela não olha view bruta: 400 mil views numa conta de 2 milhões de seguidores é um dia normal; 400 mil numa conta de 4 mil é algo que dá para copiar. Então ela ranqueia pelo **múltiplo**: views do post divididas pela mediana da própria conta. Acima de 3x é sinal.

Quem observar:

- **4 contas diretas:** mesmo nicho, mesma oferta, um pouco na sua frente.
- **4 vizinhas:** outro nicho, mesmo público. É de onde vem o formato antes de chegar no seu nicho.
- **2 a 4 grandes:** só para formato, nunca para frequência nem tom.

Prompt 1, achar e explicar:

```
/ig-viral Aqui tão 8 reels do meu nicho (IA pra pequenos negócios), com o gancho, as
views e as views normais de cada conta: [cola a lista]. Ranqueia pelo múltiplo,
explica por que os três primeiros funcionaram e tira as fórmulas de gancho.
```

Prompt 2, virar roteiro original:

```
Agora pega a fórmula que ficou em primeiro e usa o /ig-reel pra transformar num
roteiro original meu sobre este tema: [o seu tema]. Não copia a referência: mesma
estrutura, o meu ângulo, a minha voz.
```

Com um navegador conectado (Claude in Chrome, no seu próprio Chrome), a skill abre as contas e olha os reels sozinha, no ritmo de uma pessoa. Sem navegador, você rola o seu nicho normalmente e cola os links, os ganchos e as views. Nos dois casos ela nunca pede a sua senha nem entra na sua conta. Dica do autor: abra a sua coleção de Salvos, que já é referência filtrada pelo seu gosto. Rode uma vez por mês, não todo dia.

## Escrever os seus posts

Uma ideia entra, sai roteiro de reel, legenda ou carrossel. O `/ig-reel` escreve 3 ganchos, dá nota, escolhe o mais forte e monta o roteiro com o texto na tela e o tempo de cada trecho.

```
/ig-reel A minha ideia: a maioria das pessoas usa IA errado, escreve um prompt
gigante em vez de ir montando por partes. Tamanho: 30 segundos. Público: donos de
pequenos negócios que querem usar IA no dia a dia.

/ig-caption Escreve a legenda desse reel. Palavra-chave: IA no negócio. CTA: comenta
"GUIA".
```

Se a ideia rende mais em slides, troque `/ig-caption` por `/ig-carousel`.

### As ferramentas que rodam de verdade

No Claude Code, o pacote traz 5 programas em Python que rodam na sua máquina, sem internet e sem enviar nada. A partir da raiz deste repositório:

```bash
python3 .claude/skills/ig-reel/hookscore.py hooks.txt               # ranqueia os seus ganchos
python3 .claude/skills/ig-reel/beats.py script.txt --target 30      # cronometra o roteiro antes de gravar
python3 .claude/skills/ig-caption/caption.py caption.txt --keywords "ia no negocio"
python3 .claude/skills/ig-human/humanize.py draft.txt --report      # limpa e mostra cada mudança
python3 .claude/skills/ig-human/detect.py draft.txt                 # nota em 5 checagens
```

O que o próprio autor mediu: a nota de gancho é boa para matar gancho ruim antes de gravar. Para escolher entre dois ganchos bons ela quase não diferencia; quem decide é a sua retenção. O limite de hashtag que a legenda confere é 5 por post.

## Comentários e respostas

Respostas no seu post:

```
/ig-reply Esses são os comentários do meu último reel: [cola os comentários]. O meu
CTA era "comenta GUIA". Separa os comentários, escreve as respostas e o direct que
entrega o link do guia.
```

Comentar no post dos outros:

```
/ig-comment Escreve um comentário pra esse post: [cola a legenda ou descreve o
post]. Faz um que o criador fixaria de verdade.
```

## Perfil e semana

Nota e reescrita do perfil (0 a 100 em 12 critérios, reescrevendo primeiro as partes mais fracas):

```
/ig-profile Nome: [seu nome]. @: [seu @]. Bio: [cola a bio]. Link: [seu link].
Destaques: [lista]. Nicho: IA pra pequenos negócios. Objetivo: mais visita no perfil
virando seguidor.
```

A semana (rode uma vez por semana; devolve o que postar por dia, formato, horário e as 10 contas para interagir):

```
/ig-plan Planeja a minha próxima semana. Consigo postar 4 reels e 2 carrosséis. Os
melhores dias pro meu público são de terça a sábado. Tema principal da semana:
skills do Claude pra quem cria conteúdo.
```

## Humanizar e postar

Antes de qualquer legenda ou roteiro ir para o ar, passe no `/ig-human`. Ele tira as frases prontas de IA e os caracteres invisíveis que denunciam texto gerado. Depois você grava e posta.

```
/ig-human Humaniza essa legenda e me mostra o que você mudou: [cola a legenda].
```

## Referência rápida

| Quando | Roda |
| --- | --- |
| Uma vez | Instalar e preencher o `voice.md` |
| Uma vez por mês | `/ig-viral` e `/ig-audit` |
| Toda semana | `/ig-plan` |
| Todo post | `/ig-reel` ou `/ig-carousel`, `/ig-caption` e `/ig-human` |
| Depois de postar | `/ig-reply` e `/ig-dm` |

## Os erros que mais atrapalham

| Erro | Faça assim |
| --- | --- |
| Pular o `voice.md` | Sem ele, tudo sai com cara de IA. |
| Olhar view bruta | Olhe o múltiplo sobre a média da conta. |
| Copiar o reel de referência | Mesma estrutura, o seu ângulo e a sua voz. |
| Dar a sua senha para qualquer ferramenta | A skill nunca pede. Desconfie de quem pede. |
| Postar sem revisar | O humanizador limpa, mas a aprovação é sua. |

## Limites neste repositório

- O `voice.md` preenchido, listas de contas observadas, comentários de terceiros, métricas de contas e qualquer material com nome de pessoa ficam fora do repositório, conforme a [política de dados](../DATA_POLICY.md).
- Conteúdo produzido com as skills para canais institucionais segue o fluxo de [materiais educacionais](../materiais-educacionais/README.md) antes de circular com nome ou identidade visual da universidade.

## Créditos

Instagram Agent Skill por Jake Schincariol (licença MIT), <https://github.com/Jakeschincariol/instagram-agent-skill>. Prompts traduzidos e adaptados pela Deploy Club a partir do guia do autor. Esta página não é afiliada ao projeto nem ao Instagram.
