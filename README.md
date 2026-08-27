# Universidade Platform

Base open source para planejar, documentar, acompanhar e reaproveitar projetos de universidades públicas nas interfaces entre educação, saúde, pesquisa, extensão e desenvolvimento institucional.

O repositório está em fase de fundação. Seu primeiro caso de referência é o projeto **Trabalho, Autismo e Cuidado na FURG**, organizado para manter a proposta integral e, ao mesmo tempo, permitir implantação por fases factíveis.

> Este repositório não é um sistema institucional da FURG, não substitui o SisProj/SEI e não deve armazenar dados pessoais, dados de saúde, laudos, listas nominais de participantes ou documentos funcionais.

## O que foi incorporado

- estrutura reproduzível de projeto, documentação, decisões e contribuições;
- modelo compatível com os grupos de informações do SisProj: informações básicas, planejamento, equipe, metas, cronograma, receitas, despesas e documentos;
- separação explícita entre repositório público e registros institucionais protegidos;
- validação automática da estrutura, das datas, dos eixos e dos indicadores do cronograma;
- formulários para propostas de atividade e materiais educacionais;
- trilha de auditoria por issues, pull requests e registro de decisões;
- primeiro projeto-exemplo voltado a servidores autistas, servidores cuidadores e formação de gestores.

## Comece por aqui

1. Leia a [arquitetura e os limites do repositório](docs/arquitetura.md).
2. Use o [modelo de projeto para o SisProj](templates/sisproj/projeto.md).
3. Consulte o [checklist de cadastro e aprovação](projects/trabalho-autismo-cuidado-furg/checklist-sisproj.md).
4. Veja o [projeto integral Trabalho, Autismo e Cuidado na FURG](projects/trabalho-autismo-cuidado-furg/projeto.md).
5. Antes de contribuir, leia [CONTRIBUTING.md](CONTRIBUTING.md) e [SECURITY.md](SECURITY.md).

## Estrutura

```text
.
├── docs/                         arquitetura, fontes e decisões estáveis
├── templates/sisproj/            modelos reutilizáveis para novos projetos
├── projects/                     projetos concretos e seus planos públicos
├── materiais-educacionais/       fluxo de produção e revisão de recursos abertos
├── scripts/                      verificações automáticas
├── tests/                        testes das verificações
└── .github/                      colaboração, revisão e integração contínua
```

## Regra de publicação

Pode ser público: objetivos, metodologia, cronograma planejado, responsabilidades institucionais, materiais educacionais aprovados, referências públicas e resultados agregados com risco de reidentificação controlado.

Não pode ser público: nome de participante, contato, diagnóstico, laudo, prontuário, necessidade individual de adaptação, presença identificável em grupo, processo funcional/pericial, credencial, segredo, banco bruto ou ata restrita.

## Status do caso de referência

O projeto **Trabalho, Autismo e Cuidado na FURG** é uma minuta técnica para validação institucional. A classificação da ação principal, a unidade gestora, a equipe formal, as cargas horárias e as anuências ainda precisam ser confirmadas antes da submissão no SisProj. Nenhum texto deste repositório representa aprovação ou posição oficial da FURG.

## Referências e licença

A estrutura foi produzida a partir de padrões open source documentados em [referências e proveniência](docs/referencias-open-source.md), com redação e adaptação próprias. O repositório permanece sob a [licença MIT](LICENSE).

