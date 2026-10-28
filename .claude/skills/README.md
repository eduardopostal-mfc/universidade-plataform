# Skills de Claude Code do projeto

## Agência de conteúdo (método Efeito Di)

Time de 16 skills próprias da agência Consultório Digital, de Eduardo Postal (licença MIT), que produzem conteúdo de Instagram no método Efeito Di: `agencia` (orquestradora), `efeito-di` (método), `estrategia`, `espionagem`, `marca`, `roteiro`, `direcao-criativa`, `stories`, `analise`, `reel`, `editor-video`, `carrossel`, `legenda`, `perfil`, `comentarios` e `design-marketing-medico`. A `agencia` virou **agente coordenador** com um subagente por papel; ver [../agents/README.md](../agents/README.md).

- **Origem:** cópia sincronizada das skills da conta claude.ai em 2026-10-28, sem alterações de conteúdo, exceto o que segue. A `agencia` veio do `agencia.zip` do Drive (versão de 2026-10-17, que inclui o papel `design-marketing-medico`); o `templates/calendario.md` veio da cópia sincronizada, porque a entrada do zip estava corrompida.
- **`design-marketing-medico`:** reconstruída a partir do texto integral em `skills-agencia-efeito-di-orientador.md` (Drive), pois não havia cópia sincronizada. A pasta `referencias/` que ela cita (texto da Resolução CFM 2.336/2023) não foi incluída.
- **Dados removidos:** `editor-video/estudio/exemplo-gravado.json` trazia nome, CRM, RQE, WhatsApp e @ reais; foram trocados por marcadores (`[Nome completo]`, `CRM-UF 00000`, `RQE 00000`, `(00) 00000-0000`, `@seuperfil`). Na `design-marketing-medico`, o RQE do exemplo de reescrita virou `RQE 00000`.
- **Caminhos:** as skills citam `~/.claude/skills/<nome>/`; neste repositório o caminho é `.claude/skills/<nome>/`. Os agentes já fazem essa tradução.
- **Ferramentas externas:** `reel` e `editor-video` dependem de Node, Remotion, ffmpeg e Whisper na máquina da pessoa; `carrossel` depende de Playwright. Nada disso roda no GitHub Actions.
- **Dados:** a ficha preenchida (`agencia/cliente.md`), o calendário, o banco de ideias, comentários, métricas e as entregas de cada cliente ficam na pasta de trabalho do cliente, fora deste repositório, conforme a [política de dados](../../DATA_POLICY.md).

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
