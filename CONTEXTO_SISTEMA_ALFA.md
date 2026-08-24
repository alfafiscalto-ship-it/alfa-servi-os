# CONTEXTO_SISTEMA_ALFA

> Memória técnica do sistema interno Alfa Contabilidade.
> Última atualização: 24/08/2026.
> Fonte técnica desta revisão: `index.html` anexado na conversa em 24/08/2026 e confirmado como idêntico ao `index.html` do branch `main` no momento do baseline.
> Este documento deve ser lido antes de alterações relevantes no frontend.

## 1. Arquitetura

### GitHub
- É a fonte oficial do código.
- Repositório: `alfafiscalto-ship-it/alfa-servi-os`.
- Branch principal: `main`.
- O arquivo principal do sistema é `index.html`.
- Baseline funcional preservado antes desta documentação:
  - commit: `9c2dbc5cf622d22426af68f19ed6ef805eebd2fa`;
  - blob do `index.html`: `13111dd49b22700ceac5ec43f3b3eef625e13a70`;
  - branch de rollback: `backup/antes-contexto-alfa-2026-08-24`.

### Vercel
- É a plataforma definida para hospedagem/deploy do sistema.
- O fluxo esperado é GitHub -> Vercel por integração Git.
- Não fazer upload manual do `index.html` diretamente na Vercel quando a integração Git estiver funcionando.
- Após alterações no `main`, conferir o deployment automático antes de considerar a publicação concluída.

### Firebase Authentication
- Responsável pelo login com e-mail e senha.
- O frontend mantém uma lista local de e-mails autorizados e perfis.
- Essa lista local NÃO substitui o Authentication nem as regras de segurança do Firestore.
- Não apagar ou recriar usuários para corrigir problemas de frontend.

### Cloud Firestore
- Banco utilizado pelo sistema.
- NÃO utilizar Realtime Database neste projeto.
- Coleções utilizadas diretamente pelo `index.html` atual:
  - `tarefas`;
  - `clientes`;
  - `funcionarios`.
- Atualizar o frontend não recria nem apaga o banco.
- Alterações de schema/campos devem preservar documentos históricos ou ser feitas somente após análise de compatibilidade.

### Firebase Storage
- A arquitetura do projeto prevê Firebase Storage para anexos.
- PONTO DE ATENÇÃO DO BASELINE 24/08/2026: o `index.html` analisado possui `storageBucket` no `firebaseConfig` e classes CSS de anexos, mas NÃO importa o SDK `firebase-storage` e NÃO contém rotina ativa de upload/remoção de arquivos.
- Portanto, não considerar anexos funcionalmente implementados apenas porque existem estilos `.attachment-list` e `.attachment-link`.
- Qualquer implementação de anexos deve ser tratada como alteração funcional específica e testada sem apagar arquivos existentes.

---

## 2. Estrutura do sistema no `index.html`

O sistema atual é um arquivo único com HTML, CSS e JavaScript `type="module"`.

### Login
- HTML: `#loginScreen`, `#loginForm`, `#loginEmail`, `#loginPassword`.
- JavaScript principal:
  - `handleLogin()`;
  - `handleLogout()`;
  - `showApp()`;
  - `showLogin()`;
  - `startFirebase()`;
  - `onAuthStateChanged()`.

### Configuração Firebase
- Localizada no JavaScript em `const firebaseConfig`.
- SDK atual do baseline: Firebase JS `10.12.5`.
- Imports ativos:
  - `firebase-app`;
  - `firebase-auth`;
  - `firebase-firestore`.
- O objeto `firebaseConfig` deve ser preservado integralmente, salvo solicitação expressa para troca de projeto.

### Usuários e perfis
- `allowedUserEmails`: autorização adicional no frontend.
- `userProfiles`: nome, perfil e vínculo com funcionário.
- Alterações futuras em acesso devem ser coordenadas com Authentication e regras, quando expressamente autorizadas.

### Tarefas
- Interface principal: `section.board`.
- Colunas:
  - Pendente;
  - Em andamento;
  - Concluído.
- Listas:
  - `#listPendente`;
  - `#listAndamento`;
  - `#listConcluido`.
- Modal principal: `#taskModal`.
- Formulário: `#taskForm`.
- Funções relevantes:
  - `getFilteredTasks()`;
  - `renderStats()`;
  - `createTaskCard()`;
  - `renderColumn()`;
  - `render()`;
  - `openModal()`;
  - `closeModal()`;
  - `saveTask()`;
  - `handleTaskAction()`;
  - `listenTasks()`.
- Campos atuais gravados/consumidos:
  - `employee`;
  - `assignees`;
  - `clientAlias`;
  - `clientName`;
  - `clientDocument`;
  - `requestDate`;
  - `deadline`;
  - `serviceType`;
  - `description`;
  - `status`;
  - `priority`;
  - `observation`;
  - campos de auditoria como `createdAt`, `createdBy`, `updatedAt`, `updatedBy`.
- Valores de status atualmente esperados:
  - `pendente`;
  - `andamento`;
  - `concluido`.

### Clientes
- Tela: `#clientsSection`.
- Tabela: `#clientsTableBody`.
- Busca: `#clientSearchInput`.
- Cadastro: `addClient()`.
- Importação JSON: `#clientImportModal`, `parseClientsJson()`, `importClientsFromJsonText()`.
- Edição: `#clientEditModal`, `saveClientEdit()`.
- Exclusão: `deleteClient()`.
- Leitura em tempo real: `listenClients()`.
- Validação local de CPF/CNPJ:
  - `isValidCPF()`;
  - `isValidCNPJ()`;
  - `validateCpfCnpj()`;
  - `formatCpfCnpj()`.

### Equipe
- Tela: `#employeesSection`.
- Modal: `#employeeManagementModal`.
- Base local de compatibilidade: `defaultEmployees`.
- Fonte dinâmica: coleção `funcionarios`.
- Funções relevantes:
  - `mergeEmployeeRoster()`;
  - `enrichEmployeesFromTasks()`;
  - `renderEmployeesManagement()`;
  - `saveEmployeeManagement()`;
  - `toggleEmployeeActive()`;
  - `listenEmployees()`.
- Regra atual importante: funcionário inativo continua no histórico, mas não deve receber novas tarefas.

### Relatórios
- Tela: `#reportsSection`.
- Filtros:
  - mês;
  - funcionário;
  - cliente.
- Função: `generateReport()`.
- Exportação: `exportReportCsv()`.
- Regra atual do baseline: o filtro mensal considera `requestDate` (data do pedido), e não `deadline`.
- O relatório é calculado no navegador; não existe coleção de relatórios gravada por essa rotina.

### Filtros
- Busca textual: `#searchInput`.
- Status: `#statusFilter`.
- Prioridade: `#priorityFilter`.
- Funcionário: seletor da sidebar.
- Função central: `getFilteredTasks()`.

### Sidebar
- Elemento: `<aside class="sidebar">`.
- Navegação de módulos:
  - Tarefas;
  - Clientes;
  - Relatórios;
  - Equipe.
- Seletor de funcionário: `#employeeSelectorBtn`.
- Área historicamente sensível a rolagem/overflow.
- O CSS contém uma segunda camada corretiva com diversos `!important`; qualquer limpeza deve ser incremental e testada em desktop e mobile.

### Modais
- `#taskModal`;
- `#employeeSelectModal`;
- `#employeeManagementModal`;
- `#clientImportModal`;
- `#clientEditModal`.
- Regra visual importante: o body recebe `modal-is-open`.
- O cartão do modal tem rolagem interna e cabeçalho sticky.

### Backups
- Backup manual de dados: `exportBackupJson()`.
- Importação: `importBackupJsonFile()`.
- A importação pode escrever/mesclar dados em `tarefas`, `clientes` e `funcionarios`.
- Não usar importação de backup como teste.
- Rollback do código deve preferir Git/GitHub; backup JSON não substitui versionamento do frontend.

### Anexos
- O baseline contém CSS para `.attachment-list` e `.attachment-link`.
- Não foi encontrada lógica funcional de Firebase Storage no JavaScript atual.
- Ver ponto delicado específico abaixo.

---

## 3. Funcionalidades existentes no baseline

Funcionalidades efetivamente encontradas no código:
- login por Firebase Authentication;
- restrição adicional de e-mails no frontend;
- sessão acompanhada por `onAuthStateChanged`;
- visualização de tarefas em Kanban;
- múltiplos responsáveis em tarefa via `assignees`;
- compatibilidade com campo legado `employee`;
- criação e edição de tarefa;
- mudança sequencial de status:
  - Pendente -> Em andamento -> Concluído -> Pendente;
- confirmação antes de mudança de status;
- exclusão de tarefa com confirmação;
- destaques para prazo vencido, vence hoje e concluído;
- prioridades alta, média e baixa;
- busca textual;
- filtro por status;
- filtro por prioridade;
- seleção de funcionário;
- restrição de visualização para usuário não administrador conforme perfil local;
- cadastro, edição, exclusão e importação JSON de clientes;
- validação local de CPF/CNPJ;
- gestão de equipe;
- inativação sem apagar histórico;
- relatórios mensais;
- exportação CSV;
- backup manual JSON;
- importação administrativa de backup;
- listeners em tempo real para `tarefas`, `clientes` e `funcionarios`;
- tratamento visual de erro/conectividade;
- layout responsivo;
- rolagem interna dos modais;
- correção específica de rolagem da sidebar.

Não considerar como funcionalidade confirmada neste baseline:
- upload/remoção de anexos no Firebase Storage.

---

## 4. Alterações realizadas

### 24/08/2026 — Base segura de manutenção
**Objetivo:** criar memória técnica e pistas de manutenção antes de alterações funcionais maiores.

**Situação anterior**
- Não existia `CONTEXTO_SISTEMA_ALFA.md`.
- O `index.html` não possuía comentários padronizados `ALFA-DEV`.
- O histórico Git existia, mas ainda não havia uma branch específica de rollback criada para esta etapa.

**Solução aplicada**
- Identificado o baseline funcional no commit `9c2dbc5cf622d22426af68f19ed6ef805eebd2fa`.
- Confirmado que o arquivo anexado em 24/08/2026 é exatamente o mesmo blob `13111dd49b22700ceac5ec43f3b3eef625e13a70` do `main`.
- Criada a branch de rollback:
  - `backup/antes-contexto-alfa-2026-08-24`.
- Criado este arquivo de contexto.
- Adicionados comentários estratégicos `ALFA-DEV` ao `index.html`, sem alterar regras de negócio, IDs, campos do Firestore, usuários, `firebaseConfig` ou comportamento intencional.

**Partes afetadas**
- documentação do repositório;
- comentários internos do `index.html`.

**Partes NÃO alteradas**
- Firestore;
- coleções/documentos;
- Firebase Authentication;
- usuários cadastrados no Firebase;
- regras do Firestore;
- regras do Storage;
- Firebase Storage;
- `firebaseConfig`;
- nomes dos campos de tarefas/clientes/equipe.

---

## 5. Decisões técnicas permanentes

1. GitHub é a fonte oficial do código.
2. `main` é a linha de produção, salvo mudança expressamente aprovada.
3. Vercel é responsável pelo deploy/hospedagem; evitar upload manual quando a integração Git estiver disponível.
4. `index.html` deve continuar sendo o arquivo principal.
5. O banco é Cloud Firestore.
6. Não utilizar Realtime Database.
7. Atualizações do frontend não devem recriar o banco.
8. Não apagar/migrar `tarefas`, `clientes`, documentos existentes, Authentication ou Storage sem solicitação expressa.
9. Preservar o `firebaseConfig` atual.
10. Preservar IDs de elementos e nomes de campos do Firestore sempre que possível.
11. Mudanças devem ser incrementais, pequenas e testáveis.
12. Antes de alterações relevantes, criar ponto claro de rollback no Git.
13. Testes que escrevem no Firestore devem usar registros explicitamente identificados como teste e devem evitar dados reais.
14. Não fazer testes destrutivos.
15. Problemas de login devem ser investigados em frontend + Authentication + autorização/regras antes de qualquer recriação de usuário.
16. Problemas de leitura de dados devem levantar primeiro hipótese de autenticação, regras ou conectividade.
17. Problemas de layout devem ser corrigidos sem alterar schema/dados.
18. Novas funcionalidades não devem ser misturadas com refatorações estéticas não relacionadas.

---

## 6. Pontos delicados

### `firebaseConfig`
- Não alterar sem solicitação expressa.
- A presença de `storageBucket` não significa que o Storage esteja funcionalmente implementado.

### Autorização
- Existem duas camadas visíveis no frontend: `allowedUserEmails` e `userProfiles`.
- As regras reais de acesso também dependem do Firebase.
- Evitar mudanças parciais que deixem frontend e backend inconsistentes.

### Campo `employee` + `assignees`
- O sistema mantém `employee` como primeiro responsável e `assignees` como lista.
- Há lógica de compatibilidade para tarefas antigas que possuam apenas `employee`.
- Não remover um deles sem migração planejada.

### Nome de funcionários
- Nomes são usados para vínculo histórico.
- A UI bloqueia a edição do nome de funcionário existente.
- Inativar é preferível a excluir/renomear.

### Clientes
- Dados do cliente também são copiados para tarefas (`clientAlias`, `clientName`, `clientDocument`).
- Excluir o cadastro do cliente não apaga tarefas históricas.
- Alterações futuras devem considerar essa duplicação intencional para histórico.

### Relatórios
- Atualmente usam `requestDate`.
- Trocar para `deadline` ou oferecer ambos deve ser uma melhoria separada e explicitamente testada.

### Data local
- `todayISO()` usa `new Date().toISOString().slice(0, 10)`, portanto calcula a data por UTC.
- Em horários próximos da virada UTC isso pode divergir do dia local do escritório.
- Correção recomendada em alteração funcional separada; não foi modificada nesta etapa.

### Sidebar / overflow
- O CSS possui regras originais e uma camada corretiva posterior com `!important`.
- É área com histórico de problemas de rolagem.
- Não remover essas regras em uma limpeza ampla sem teste visual.

### Modais
- Dependem de `body.modal-is-open`, `max-height`, `overflow-y` e cabeçalho sticky.
- Testar especialmente o modal de Novo serviço em telas menores.

### Backup JSON
- A importação escreve no Firestore.
- Deve permanecer administrativa.
- Não confundir rollback de código (Git) com restauração de dados (JSON).

### Firebase Storage / anexos
- Integração não encontrada no JavaScript do baseline.
- Não criar/alterar regras de Storage nesta etapa.
- Antes de implementar, confirmar estrutura desejada dos caminhos, metadados da tarefa e compatibilidade com arquivos já existentes.

---

## 7. Próximas melhorias

As próximas melhorias devem ser tratadas uma de cada vez.

### Prioridade técnica
1. Confirmar e documentar o projeto/deploy de produção da Vercel conectado a este repositório.
2. Corrigir `todayISO()` para respeitar a data local do escritório sem alterar datas já gravadas.
3. Revisar a arquitetura de anexos/Storage em alteração isolada, porque o baseline não contém implementação funcional.
4. Reduzir progressivamente CSS corretivo duplicado, somente depois de testes visuais de regressão.

### Prioridade de usabilidade — propostas ainda não implementadas neste baseline
- tela inicial orientada a vencidos, vencimentos de hoje e próximos prazos;
- modo de lista além do Kanban;
- visão por prazo/calendário;
- ficha operacional do cliente com tarefas relacionadas;
- relatório opcional por data do pedido ou prazo limite;
- organização das ferramentas administrativas fora da barra principal;
- busca global mais ampla.

Cada item acima deve ser aprovado e implementado separadamente para evitar regressões.

---

## Checklist antes de futuras publicações

- [ ] Ler este arquivo.
- [ ] Trabalhar a partir do `index.html` fornecido/confirmado como atual.
- [ ] Confirmar o commit/branch funcional de origem.
- [ ] Criar rollback antes de alteração relevante.
- [ ] Preservar `firebaseConfig`.
- [ ] Não alterar Firestore/Authentication/Storage/regras sem autorização expressa.
- [ ] Validar sintaxe JavaScript.
- [ ] Conferir IDs dos elementos alterados.
- [ ] Conferir login.
- [ ] Conferir leitura de tarefas.
- [ ] Conferir criação/edição/status sem usar dados reais.
- [ ] Conferir clientes.
- [ ] Conferir filtros.
- [ ] Conferir relatórios.
- [ ] Conferir modais e rolagens.
- [ ] Conferir desktop e mobile.
- [ ] Atualizar este Markdown.
- [ ] Atualizar comentários `ALFA-DEV` se necessário.
- [ ] Publicar via GitHub.
- [ ] Conferir deployment da Vercel.
- [ ] Registrar commit publicado e resultado do deploy.
