# Como contribuir

Contribuições podem aperfeiçoar modelos, documentação, validações e materiais educacionais. O objetivo é manter os projetos claros, auditáveis, acessíveis e compatíveis com os fluxos institucionais.

## Fluxo recomendado

1. Abra uma issue e descreva a necessidade, o público afetado e o resultado esperado.
2. Crie uma branch curta e específica.
3. Faça alterações pequenas, com fontes públicas próximas das afirmações materiais.
4. Execute `python3 scripts/validate_repository.py` e `python3 -m unittest discover -s tests`.
5. Abra um pull request e complete todos os itens aplicáveis do checklist.

## Requisitos de conteúdo

- diferencie fato verificado, proposta, hipótese e decisão pendente;
- informe a fonte, a data da consulta e o escopo de qualquer norma ou evidência;
- use linguagem respeitosa, acessível e não patologizante;
- não prometa cuidado clínico, direito funcional ou aprovação institucional;
- garanta alternativa textual para imagens e estrutura navegável por títulos;
- registre mudanças relevantes no arquivo de decisões do projeto correspondente.

## Proteção de dados

Nunca envie ao GitHub dados pessoais ou de saúde, mesmo em issues privadas ou pull requests. Não são aceitos:

- nomes, contatos, matrículas, SIAPE ou listas de presença;
- diagnósticos, laudos, prontuários ou informações periciais;
- relatos que permitam identificar participantes;
- exportações de formulários, planilhas brutas ou atas restritas;
- credenciais, chaves, tokens ou arquivos `.env`.

Use dados sintéticos em testes e apenas resultados agregados em documentação pública. Em grupos pequenos, não publique cruzamentos que possibilitem reidentificação.

## Critério de conclusão

Uma contribuição só está pronta quando o conteúdo, a fonte, a privacidade, a acessibilidade, a responsabilidade e a forma de validação estiverem explícitos. Aprovação em pull request não substitui anuência de chefia, aprovação no SisProj, análise ética ou decisão administrativa quando forem exigidas.

