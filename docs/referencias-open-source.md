# Referências open source e proveniência

Consulta realizada em 27 de agosto de 2026. A incorporação foi conceitual e seletiva: não foi feito clone integral nem cópia indiscriminada de arquivos. A redação e a implementação deste repositório são próprias.

## Repositórios analisados

| Referência | Licença identificada | Elementos aproveitados | Decisão de adaptação |
| --- | --- | --- | --- |
| [The Turing Way — Reproducible Project Template](https://github.com/the-turing-way/reproducible-project-template) | MIT para software e CC BY 4.0 para documentação | separação de gestão, comunicação, relatórios, contribuição e código de conduta | estrutura simplificada para projetos institucionais; nenhum conteúdo copiado literalmente |
| [DTU Digital Health — Reproducible Project Template](https://github.com/dtu-digital-health/reproducible-project-template) | MIT para código e CC BY 4.0 para documentação | organização reproduzível para educação e saúde digital | dados reais foram excluídos do desenho público; foco deslocado de análise de dados para governança do projeto |
| [CDCgov — Template](https://github.com/CDCgov/template) | Apache-2.0 | práticas abertas, revisão de segurança, proibição de PII/PHI, manutenção e templates de colaboração | avisos próprios do CDC não foram reutilizados; os controles foram reescritos para o contexto universitário brasileiro |
| [Public Health Scotland — phstemplates](https://github.com/Public-Health-Scotland/phstemplates) | MIT | política conservadora para impedir versionamento acidental de dados e planilhas | o `.gitignore` foi adaptado sem bloquear os CSV públicos de modelos e cronogramas |
| [Open Research Data Template](https://github.com/maehr/open-research-data-template) | AGPL-3.0 para software e CC BY para conteúdo conforme arquivos do projeto | citação, segurança, registro de marcos e rastreabilidade | ideias gerais adotadas; nenhum código AGPL foi incorporado |

## Fontes oficiais da FURG usadas no modelo

- [Manual dos passos básicos do Cadastro no SisProj](https://propesp.furg.br/images/arquivos_propesp/DIPESQ/Cadastro-no-SisProj-Responsveis-pelo-projeto-.pdf): grupos de informações, equipe, metas, cronograma, indicadores, receitas, despesas, submissão e aprovação.
- [Página institucional sobre o SisProj](https://propesp.furg.br/pt/passos-basicos-de-cadastro-de-projetos-no-sisproj): finalidade do sistema unificado e fluxo pela unidade gestora e pró-reitoria correspondente.
- [Edital Pró-Extensão 2026](https://eqa.furg.br/images/Edital_N__2026.pdf): critérios atuais de consistência, impacto social, participação discente, indissociabilidade e viabilidade orçamentária. Os critérios do edital não são tratados como regra universal para toda modalidade.

## Regras de interpretação

- A existência de um campo no modelo não determina a modalidade principal do projeto.
- O manual público do SisProj orienta o cadastro, mas a interface e os procedimentos podem mudar; a conferência final deve ocorrer no sistema e com a unidade competente.
- Critérios de edital só se aplicam quando a proposta concorre ao edital correspondente.
- Referência open source é padrão de engenharia, não autoridade clínica, jurídica ou administrativa.

