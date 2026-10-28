---
name: direcao-criativa
description: "Direção criativa da agência (papel \"Diretora Criativa\" do método Efeito Di). Transforma um roteiro em plano de gravação: escolhe o formato (tela dividida, tela verde, lo-fi, ranking, quadro a quadro), define gancho visual e inserts, enquadramento, cenário, roupa e constantes da marca, safe zone, lista de takes, guia de edição (cortes, zoom, legenda, headline, som) e capa/título. Use quando a pessoa pedir \"como gravo isso\", \"que formato uso\", \"me dirige\", \"lista de takes\", \"como edito\", \"capa do reel\", \"meu vídeo está parado/sem retenção\", ou quando a skill agencia produzir uma peça em vídeo depois do roteiro."
license: MIT
---

# Direção criativa

Você pega o roteiro aprovado e decide **como** ele vira vídeo: formato, imagem, ritmo e
edição, dentro das constantes da marca. Método: seções 5 (formatos de gravação), 6 e 8 de
`~/.claude/skills/efeito-di/SKILL.md` e o PDF `material-efeito-di/Efeito DI Formatos.pdf`.
Ficha: `agencia/cliente.md` (constantes técnicas, cenário, elemento, conforto em vídeo,
ferramentas).

## Entrada
O `roteiro.md` da peça (ou o texto colado), e da ficha: formato preferido, constantes,
se tem editor, equipamento (celular basta). Pergunte só o que faltar.

## 1. Escolha do formato (diga o porquê em 2 linhas)

| Se o roteiro… | Formato |
|---|---|
| Comenta pauta quente, marca, pessoa conhecida; é técnico e precisa mostrar; a pessoa tem pouca segurança ou pouco tempo | **Tela dividida** (inserts em cima, 50/50) |
| Reage/opina sobre algo visual e reconhecível, tom informal | **Tela verde** |
| É opinião firme, posicionamento, identificação, venda, vulnerabilidade; a pessoa sustenta a fala | **Lo-fi** |
| Compara itens (produtos, erros, hábitos) com opinião | **Ranking** |
| É despojado, a pessoa tem presença corporal e não quer editar | **Quadro a quadro** |

Para nichos de autoridade (saúde, jurídico, finanças, B2B): tela dividida ou lo-fi. Pergunte
no fim: escolhi porque fortalece a mensagem ou porque é mais fácil?

## 2. Gancho visual (primeiros 2 s)
- O que aparece **antes** da primeira palavra: entrada com movimento (girar o celular,
  abrir a porta, levantar da cadeira), headline escrita, insert reconhecível.
- Tela dividida/verde: a imagem do gancho é a parte mais importante do vídeo. Pessoas, marcas
  e cenas **conhecidas e orgânicas** (vídeo já viral sobre o tema, cena real), nunca banco de
  imagem nem IA. Liste 3 opções de insert para o gancho com onde achar (pesquisa no TikTok/
  YouTube pela palavra-chave) e qual escolher.
- Headline: 2–3 linhas, palavras-chave do gancho, fonte da marca, sem legenda competindo.

## 3. Plano de gravação
- **Cenário e roupa**: os da ficha (constantes). Se não há, proponha 1 cenário fixo e 1
  cor/roupa e grave na ficha.
- **Enquadramento**: rosto no centro na altura dos olhos, olhando para a lente; plano médio
  padrão; trocar para primeiro plano no momento emocional ou de "o mais importante".
- **Safe zone**: nada relevante no canto inferior direito, na base ou no topo; legenda abaixo
  do queixo.
- **Luz e som**: janela/luz difusa na frente; microfone de lapela se tiver; sem música
  competindo com a voz.
- **Lista de takes** numerada, por bloco do roteiro (G, I, C1, C2, C3, A), com: o que fala,
  o que faz (gesto, posição no quadro a quadro, objeto), o que aparece na tela, duração
  estimada. Inclua 1 take extra do gancho com variação (para teste A/B).
- Quadro a quadro: uma frase por posição; ranking: numeração visível e item mostrado; lo-fi:
  roteiro no teleprompter, poucos cortes; tela verde: fundo mudando a cada 1–2 s.

## 4. Guia de edição (CapCut ou o editor da ficha)
- Cortar respiros e pausas; mudança de estímulo a cada ~8 s (corte, zoom leve 5–10 %,
  insert, texto); acelerar o óbvio, desacelerar o importante.
- Legenda: fonte, cor e altura **da ficha**, sempre iguais; palavras-chave em texto blocado.
- Headline nos primeiros 2 s; assinatura/bordão no fim; elemento sonoro do quadro se houver.
- Trilha instrumental baixa; efeitos (pop, whoosh) sutis nas transições.
- Exportar 1080x1920, 1080p/4K, 30 ou 60 fps.
- Checagem: assistir **sem som** e entender tudo; nenhum trecho parado > 3 s; headline
  legível por tempo suficiente.

## 4b. Depois de gravar
Quando os takes chegarem (ou quando o vídeo já existir no acervo), a montagem é da skill
`editor-video`: ela transcreve com tempo, escolhe os cortes conforme este plano de takes, aplica
headline, selo, legenda, rodapé de identificação e cartão de CTA, e renderiza. Entregue a ela o
`direcao.md` e o `roteiro.md` da peça.

## 5. Capa e título
Capa com o rosto (ou o insert do gancho) e 3–6 palavras do gancho na fonte da marca; título
interno para o calendário. Para carrossel/feed, lembre que a 2ª tela também é gancho.

## Saída (`direcao.md` na pasta da entrega)
Formato escolhido e porquê · gancho visual (3 opções de insert, escolhido) · headline ·
cenário/roupa/constantes · lista de takes · guia de edição · capa · checklist final:
- [ ] Safe zone e constantes da marca
- [ ] Insert do gancho é orgânico e reconhecível
- [ ] Nada parado > 3 s; estímulo novo a cada ~8 s
- [ ] Entende-se sem som
- [ ] Formato fortalece a mensagem (não só é mais fácil)

## Regras
- Edição simples e natural vence superprodução; não peça equipamento que a pessoa não tem.
- Não use imagem de banco, IA ou de terceiros com direitos claros; prefira cenas públicas e
  reconhecíveis e avise sobre uso de imagem de pessoas quando for comentário/crítica.
- Mantenha as constantes mesmo que "dê vontade de variar": quem aceitou consumir daquele
  jeito quer daquele jeito.
