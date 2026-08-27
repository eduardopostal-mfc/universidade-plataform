# Arquitetura documental e limites

## Finalidade

O Universidade Platform organiza a construção de projetos institucionais sem confundir colaboração pública com registro administrativo. O GitHub documenta versões, decisões, modelos e materiais abertos; os sistemas oficiais preservam a autoridade, os documentos e os dados protegidos.

## Duas camadas

| Camada pública no GitHub | Camada institucional protegida |
| --- | --- |
| modelos de projeto e cronograma | cadastro e plano de trabalho oficial no SisProj |
| objetivos, metodologia e responsabilidades propostas | atas, anuências, cargas horárias e documentos de aprovação |
| referências públicas e registro de decisões sanitizado | processos SEI e comunicações administrativas restritas |
| materiais educacionais aprovados | listas de participantes, contatos e necessidades individuais |
| indicadores vazios e resultados agregados seguros | respostas individuais, presença e instrumentos brutos |
| código, testes e schemas sem dados reais | dados pessoais, dados de saúde, laudos e documentos periciais |

O GitHub nunca é a fonte oficial para concessão de direito, decisão pericial, atendimento clínico ou aprovação institucional.

## Unidades documentais

### `templates/`

Contém estruturas reutilizáveis. Um modelo não expressa aprovação e deve ser adaptado à modalidade, à unidade gestora e às regras vigentes.

### `projects/`

Cada projeto possui um diretório com:

- `project.json`: metadados estruturados e eixos de trabalho;
- `projeto.md`: proposta integral;
- `cronograma.csv`: atividades, responsáveis e indicadores físicos;
- `matriz-responsabilidades.md`: decisão e execução por papel;
- `monitoramento-avaliacao.md`: indicadores, fontes e salvaguardas;
- `governanca-lgpd.md`: limites, dados e controle institucional;
- `checklist-sisproj.md`: lacunas e fluxo até a submissão.

### `materiais-educacionais/`

Contém apenas recursos aprovados para circulação aberta e suas regras de revisão. Materiais clínicos ou jurídicos exigem fonte primária, data de revisão e responsável institucional.

## Ciclo de mudança

1. Uma necessidade é registrada em issue sem dados pessoais.
2. A alteração é produzida em branch.
3. O pull request registra fonte, impacto, privacidade e acessibilidade.
4. A validação automática verifica estrutura e coerência básica.
5. Revisores verificam conteúdo e competência institucional.
6. A versão pública é mesclada; a versão oficial segue o fluxo próprio no SisProj/SEI.

## Controle de versões

O histórico Git registra a evolução pública, mas não deve ser usado para versionar informação que precise ser apagada por obrigação legal ou operacional. Dados sujeitos a correção, retenção limitada ou sigilo devem permanecer em sistema institucional apropriado.

## Princípios técnicos

- dados mínimos e finalidade explícita;
- nenhum segredo ou dado sensível no repositório;
- fonte próxima da afirmação;
- responsabilidade humana identificada;
- acessibilidade desde o desenho;
- mudanças revisáveis e reversíveis;
- resultados agregados com avaliação de risco de reidentificação;
- distinção entre proposta, execução, aprovação e evidência de resultado.

