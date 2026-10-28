# Skills de Claude Code do projeto

## `agencia` (Efeito Di)

Orquestradora da agência de conteúdo para Instagram montada sobre o método Efeito Di: faz o onboarding do cliente numa ficha única, escolhe o fluxo (onboarding, pauta da semana, produção de peça, semana de venda, revisão mensal, pedido solto) e aciona as skills de papel na ordem certa, com controle de qualidade no fim.

- **Origem:** skill própria da agência Consultório Digital, de Eduardo Postal (licença MIT), copiada em 2026-10-28 do pacote `agencia.zip` da pasta "skills-zip" do Drive (versão de 2026-10-17, que inclui o papel `design-marketing-medico`). O `templates/calendario.md` veio da cópia sincronizada na conta claude.ai, porque a entrada do zip estava corrompida.
- **Arquivos:** `agencia/SKILL.md`, `agencia/templates/cliente.md` (ficha do cliente, vazia) e `agencia/templates/calendario.md` (calendário editorial, vazio).
- **Dependências não incluídas:** a skill delega para `efeito-di`, `estrategia`, `espionagem`, `marca`, `roteiro`, `direcao-criativa`, `stories`, `analise`, `reel`, `editor-video`, `carrossel`, `legenda`, `perfil`, `comentarios` e `design-marketing-medico`. Nenhuma delas está neste repositório; sem elas a `agencia` funciona como roteiro de atendimento, mas não consegue acionar os papéis.
- **Dados:** a ficha preenchida (`agencia/cliente.md`), o calendário, o banco de ideias e as entregas ficam na pasta de trabalho de cada cliente, fora deste repositório, conforme a [política de dados](../../DATA_POLICY.md).

## Skills de Instagram (`/ig-*`)

Pacote de 13 skills para Claude Code que escrevem roteiros de reels, legendas,
carrosséis, stories, comentários, respostas, DMs, plano semanal, auditoria e
perfil, mais um humanizador. Nada é publicado automaticamente: as skills escrevem,
quem aprova e posta é a pessoa.

- **Origem:** <https://github.com/Jakeschincariol/instagram-agent-skill>
- **Autor:** Jake Schincariol
- **Versão incorporada:** commit `d03c56b` (plugin 1.0.0), copiada em 2026-10-28
  sem alterações nos arquivos de cada skill.
- **Guia em português:** [docs/skills-instagram-claude.md](../../docs/skills-instagram-claude.md)
- **Perfil de voz:** modelo em [../instagram/voice.md](../instagram/voice.md);
  copie para `~/.claude/instagram/voice.md` e preencha.

## Atualizar

```bash
git clone --depth 1 https://github.com/Jakeschincariol/instagram-agent-skill /tmp/ig
rm -rf .claude/skills/ig-*
cp -r /tmp/ig/skills/ig-* .claude/skills/
```

Depois atualize o commit registrado acima e rode `python3 scripts/validate_repository.py`.

## Licença do pacote

    MIT License
    
    Copyright (c) 2026 Jake Schincariol
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
