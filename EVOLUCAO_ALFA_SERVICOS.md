# Alfa Serviços — roteiro permanente de evolução

> Documento de continuidade técnica / auto-prompt do projeto.
> Antes de alterar o sistema, leia este arquivo e depois procure no `index.html` pelos marcadores `ALFA-ARCH`, `ALFA-DATA-CONTRACT`, `ALFA-CHANGELOG` e `ALFA-NEXT`.

## 1. Objetivo do sistema

Transformar o Alfa Serviços em uma central operacional interna da Alfa Contabilidade: o sistema deve dizer com clareza **o que precisa ser feito, por quem, para qual cliente e até quando**, mantendo histórico, produtividade e segurança.

O sistema é hospedado no GitHub Pages e usa Firebase Authentication + Cloud Firestore. O arquivo principal continua sendo `index.html`.

## 2. Regra de ouro: preservar os dados

Mudanças visuais e de arquitetura do front-end não podem alterar, apagar, migrar ou renomear dados existentes sem solicitação expressa do usuário.

Contrato atual que deve ser tratado como estável:

- coleção `tarefas`;
- coleção `clientes`;
- coleção `funcionarios`;
- IDs de documentos existentes;
- campos já existentes nas tarefas, clientes e funcionários;
- `firebaseConfig` do projeto atual;
- autenticação por e-mail e senha;
- perfis e usuários autorizados já existentes.

Uma evolução pode **ler e cruzar** os dados existentes para gerar dashboards, listas, filtros, relatórios e indicadores sem gravar novos campos.

## 3. Regra de trabalho para futuras alterações

1. Sempre usar como base o `index.html` que o usuário anexar na conversa atual. Nunca reconstruir a partir de uma versão antiga do chat.
2. Antes de editar, localizar e ler os comentários de continuidade dentro do próprio `index.html`.
3. Não trocar o projeto Firebase nem o `firebaseConfig`, salvo pedido explícito.
4. Não mudar nomes das coleções ou estrutura dos documentos existentes sem necessidade comprovada e autorização explícita.
5. Não deixar regras do Firestore abertas para qualquer pessoa.
6. Fazer alterações incrementais e reversíveis.
7. Preservar funcionalidades que já funcionam.
8. Priorizar produtividade de escritório: prazo, prioridade, cliente, responsável e situação devem ser visíveis rapidamente.
9. Depois de uma alteração relevante, registrar um comentário `ALFA-CHANGELOG` no código e atualizar este MD.
10. Sempre manter um ponto de restauração no GitHub antes de mudanças grandes.

## 4. Pistas obrigatórias dentro do código

O `index.html` deve conter comentários pesquisáveis para orientar a próxima manutenção.

### `ALFA-ARCH`
Explica arquitetura de uma área e por que ela existe.

Exemplo:

```html
<!-- ALFA-ARCH: Dashboard usa somente dados já carregados do Firestore. Não cria documentos. -->
```

### `ALFA-DATA-CONTRACT`
Marca trechos que não podem ter nomes de coleção/campos alterados casualmente.

Exemplo:

```js
// ALFA-DATA-CONTRACT: manter coleções tarefas, clientes e funcionarios.
```

### `ALFA-CHANGELOG`
Registra alterações relevantes, com data e versão.

Exemplo:

```js
// ALFA-CHANGELOG 2026-08-24 v2.0.0: criado painel Início sem alterar esquema do Firestore.
```

### `ALFA-NEXT`
Registra melhorias planejadas que ainda não devem ser implementadas sem avaliação.

Exemplo:

```js
// ALFA-NEXT: calendário mensal de prazos reutilizando task.deadline.
```

Esses marcadores devem ser mantidos nas versões futuras. Quando uma melhoria `ALFA-NEXT` for concluída, ela deve virar `ALFA-CHANGELOG`.

## 5. Arquitetura desejada do front-end

Mesmo que o sistema continue em um único HTML, a lógica deve ser pensada em camadas:

```text
Firebase / Firestore
        ↓
carregamento e escrita de dados
        ↓
estado local: tasks / clients / employees
        ↓
seletores e cálculos derivados
        ↓
views e componentes visuais
```

Evitar espalhar regras de negócio pela interface. Sempre que possível, criar helpers reutilizáveis para:

- tarefas visíveis pelo usuário;
- vencidas;
- vencem hoje;
- próximos vencimentos;
- prioridade alta;
- tarefas por funcionário;
- tarefas por cliente;
- indicadores mensais.

## 6. Roadmap

### Etapa 0 — segurança e continuidade
Status: concluída em 24/08/2026.

- criar branch de backup antes da evolução 2.0;
- criar este MD;
- inserir marcadores de continuidade no `index.html`;
- preservar banco e `firebaseConfig`.

### Etapa 1 — central operacional
Status: em implantação em 24/08/2026.

Objetivo: tornar o sistema útil já no primeiro acesso sem alterar o Firestore.

- criar módulo **Início**;
- mostrar vencidas, vencem hoje, próximos 7 dias, alta prioridade e em andamento;
- criar acesso rápido **Minha fila**;
- manter Kanban;
- adicionar visualização **Lista** para tarefas;
- priorizar visualmente cliente, serviço, responsável e prazo;
- ordenar tarefas de forma mais útil por urgência;
- corrigir cálculo de data atual para data local do navegador;
- mover backup, restauração e alteração de senha para **Administração**;
- permitir relatório por **Data do pedido** ou **Prazo limite**;
- criar painel operacional de cliente usando as tarefas existentes.

### Etapa 2 — produtividade e navegação
Status: planejada.

- calendário mensal/semanal por `deadline` sem necessidade de novos campos;
- busca global com atalho `Ctrl + K`;
- filtros rápidos: vencidas, hoje, semana, alta prioridade;
- persistir preferência de visualização no `localStorage`;
- detalhes de tarefa em painel lateral em vez de excesso de informação no cartão;
- melhorar responsividade em notebooks menores.

### Etapa 3 — arquitetura interna
Status: planejada.

- reduzir CSS duplicado e dependência de `!important`;
- agrupar estilos por componente;
- organizar JavaScript por módulos lógicos dentro do mesmo arquivo ou, se autorizado, separar em arquivos estáticos sem alterar Firestore;
- criar uma camada única para operações de `tarefas`, `clientes` e `funcionarios`;
- reduzir chamadas diretas ao Firestore espalhadas pelo código;
- padronizar tratamento de erros e loading states.

### Etapa 4 — gestão avançada
Status: futura; avaliar antes de qualquer mudança de banco.

Possibilidades que podem exigir novos campos e, portanto, **não devem ser implementadas automaticamente**:

- histórico detalhado de mudança de status;
- comentários por tarefa;
- checklist/subtarefas;
- data/hora real de conclusão;
- recorrência automática de obrigações;
- notificações automáticas;
- anexos via Firebase Storage;
- SLA e tempo médio de execução.

Qualquer item desta etapa deve ser discutido antes porque pode mudar o contrato de dados.

## 7. Critérios de qualidade

Uma versão só deve ser considerada boa se:

- login continua funcionando;
- tarefas antigas continuam aparecendo;
- criar/editar/iniciar/concluir/reabrir tarefa continua funcionando;
- clientes continuam carregando;
- equipe continua carregando;
- relatórios continuam funcionando;
- nenhum dado existente é removido ou renomeado;
- telas não ficam cortadas;
- modal Novo serviço continua com rolagem interna;
- navegação funciona em desktop e celular;
- erros do Firestore continuam sendo explicados de forma legível;
- uma futura manutenção consegue entender as decisões pelos marcadores no código e por este MD.

## 8. Backup e restauração da evolução 2.0

Antes da primeira implantação 2.0 foi criada a branch:

`backup/pre-alfa-2-0-2026-08-24`

Ela deve ser tratada como ponto de restauração da versão anterior à evolução de arquitetura iniciada em 24/08/2026.

## 9. Instrução curta para a próxima IA/manutenção

Leia este MD inteiro. Depois abra o `index.html` atual e pesquise os marcadores `ALFA-ARCH`, `ALFA-DATA-CONTRACT`, `ALFA-CHANGELOG` e `ALFA-NEXT`. Preserve o contrato do Firestore e o `firebaseConfig`. Evolua primeiro a interface e os cálculos derivados. Não crie migração, coleção ou campo novo apenas por conveniência. Registre no código e neste MD o que foi alterado e mantenha uma restauração disponível antes de mudanças grandes.
