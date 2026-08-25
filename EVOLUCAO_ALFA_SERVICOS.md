# Alfa Serviços — roteiro permanente de evolução

> Documento oficial de roadmap e continuidade das evoluções do sistema interno da Alfa Contabilidade.
> Última atualização: 25/08/2026 (America/Sao_Paulo).
> Este arquivo deve ser mantido e atualizado a cada etapa relevante concluída.

## 1. Função deste documento

Este arquivo responde principalmente a quatro perguntas:

1. O que já foi concluído?
2. Qual é a próxima etapa aprovada?
3. Qual é a ordem planejada das próximas melhorias?
4. Quais regras de segurança devem ser respeitadas durante a evolução?

Ele deve ser usado em conjunto com:

- `CONTEXTO_SISTEMA_ALFA.md` — memória técnica do funcionamento atual;
- `index.html` — código principal do sistema;
- comentários `ALFA-DEV` — pistas técnicas inseridas nos pontos críticos do código.

### Regra de separação

- `CONTEXTO_SISTEMA_ALFA.md` registra **como o sistema funciona atualmente**.
- `EVOLUCAO_ALFA_SERVICOS.md` registra **o que será melhorado e em qual ordem**.
- `index.html` contém o código efetivamente utilizado em produção.

---

## 2. Objetivo do sistema

Transformar gradualmente o Alfa Serviços em uma central operacional interna profissional da Alfa Contabilidade.

O sistema deve permitir que a equipe identifique rapidamente:

- o que precisa ser feito;
- para qual cliente;
- quem é o responsável;
- qual é o prazo;
- qual é a prioridade;
- o que está vencido;
- o que precisa de atenção hoje;
- o que já foi concluído.

A evolução deve seguir a ordem de prioridade:

**SEGURANÇA → ESTABILIDADE → ORGANIZAÇÃO → USABILIDADE → NOVAS FUNCIONALIDADES → ESTÉTICA**

---

## 3. Arquitetura oficial do projeto

### Código e versionamento

**GitHub**

- fonte oficial do código;
- repositório: `alfafiscalto-ship-it/alfa-servi-os`;
- branch de produção: `main`;
- arquivo principal: `index.html`.

### Hospedagem e deploy

**Vercel**

Fluxo correto:

```text
index.html atual
      ↓
branch de trabalho no GitHub
      ↓
Preview da Vercel
      ↓
testes
      ↓
merge no main
      ↓
deploy automático da Vercel
      ↓
produção
```

Não realizar upload manual do site diretamente na Vercel quando a integração Git estiver funcionando.

### Login

**Firebase Authentication — acesso compartilhado**

- o Firebase Authentication continua sendo a barreira técnica de segurança;
- desde a versão `1.8.0`, o frontend usa uma única conta técnica do escritório: `alfafiscalto@gmail.com`;
- a tela de login pede somente a senha do escritório;
- funcionários não precisam mais possuir usuário próprio no Firebase;
- a seleção de Henrique, David, Amanda, Flavia, Joyce, Julyana, Laila, Mariana ou Todos é operacional e acontece na interface;
- usuários antigos do Authentication não foram apagados automaticamente e podem permanecer cadastrados;
- nunca substituir essa simplificação por regras públicas de Firestore.

### Banco de dados

**Cloud Firestore**

Coleções utilizadas pelo sistema atual:

- `tarefas`;
- `clientes`;
- `funcionarios`.

Não utilizar Realtime Database.

### Anexos

**Firebase Storage** é a tecnologia prevista para anexos.

Entretanto, no baseline analisado em 24/08/2026, o `index.html` possui `storageBucket` no `firebaseConfig` e estilos visuais de anexos, mas **não possui integração funcional de upload com o Firebase Storage**.

Por isso, anexos devem ser tratados como uma etapa funcional futura específica e não como uma funcionalidade já confirmada.

---

## 4. Contrato de segurança dos dados

Alterações de frontend NÃO devem automaticamente:

- apagar documentos;
- recriar banco;
- migrar coleções;
- renomear coleções;
- renomear campos existentes;
- trocar projeto Firebase;
- trocar `firebaseConfig`;
- alterar Firebase Authentication;
- apagar usuários;
- alterar regras do Firestore;
- alterar regras do Storage;
- apagar anexos.

Contrato atual a preservar:

- coleção `tarefas`;
- coleção `clientes`;
- coleção `funcionarios`;
- IDs existentes;
- campos existentes;
- `firebaseConfig` atual;
- conta técnica compartilhada autorizada;
- autenticação por e-mail e senha no Firebase, sem vínculo entre e-mail e funcionário.

Uma melhoria pode ler, filtrar, ordenar e cruzar os dados existentes no navegador sem modificar o banco.

---

## 5. Regra obrigatória de trabalho

Para cada alteração funcional relevante:

1. utilizar exclusivamente o `index.html` atual anexado pelo usuário na conversa correspondente;
2. ler `CONTEXTO_SISTEMA_ALFA.md`;
3. ler este `EVOLUCAO_ALFA_SERVICOS.md`;
4. localizar os comentários `ALFA-DEV` relevantes no código;
5. confirmar qual commit do `main` está funcional;
6. criar um ponto de rollback antes da alteração;
7. criar branch de trabalho separada;
8. implementar apenas a etapa aprovada;
9. não misturar melhorias estruturais não relacionadas;
10. validar sintaxe e estrutura do HTML/JavaScript;
11. revisar o diff antes de publicar;
12. publicar a branch no GitHub;
13. conferir Preview da Vercel;
14. realizar testes não destrutivos;
15. somente depois fazer merge no `main`;
16. conferir o deployment de produção da Vercel;
17. atualizar `CONTEXTO_SISTEMA_ALFA.md` quando o funcionamento atual mudar;
18. atualizar este roteiro quando uma etapa for concluída;
19. atualizar/adicionar comentários `ALFA-DEV` nos pontos críticos alterados.

### Testes com Firestore

Nunca usar dados reais desnecessariamente para testes.

Quando uma gravação for indispensável:

- utilizar registro claramente identificado como teste;
- evitar qualquer alteração destrutiva;
- remover somente o próprio registro de teste se isso puder ser feito com segurança;
- nunca testar importação de backup em produção apenas para validar interface.

---

## 6. Estado atual do projeto

### Baseline funcional anterior à documentação

Commit:

`9c2dbc5cf622d22426af68f19ed6ef805eebd2fa`

Blob do `index.html` confirmado:

`13111dd49b22700ceac5ec43f3b3eef625e13a70`

### Rollback preservado

Branch:

`backup/antes-contexto-alfa-2026-08-24`

Essa branch deve continuar preservada como ponto de retorno anterior à criação da nova base documental.

### Produção após a Etapa 0

Commit publicado:

`9c4cfd5d3b619944611012db26cf803c2bee4265`

Alterações desse commit:

- criação de `CONTEXTO_SISTEMA_ALFA.md`;
- comentários estratégicos `ALFA-DEV` no `index.html`;
- nenhuma alteração funcional no Firestore;
- nenhuma alteração no `firebaseConfig`;
- nenhuma alteração em usuários;
- nenhuma mudança de schema;
- deploy de produção confirmado com status de sucesso pela integração Vercel/GitHub.

### Produção após a Etapa 1

Commit funcional publicado:

`5ac984554f046ba68e62da923e7ea72ff3cb6097`

Rollback preservado antes da Etapa 1:

`backup/antes-dashboard-inicio-2026-08-24`

Alterações funcionais:

- versão visual `1.7.0`;
- novo módulo **Início** como primeira tela após o login;
- indicadores de tarefas vencidas, vencem hoje, próximos 3 dias, alta prioridade e em andamento;
- listas de atenção e próximos prazos;
- resumo da equipe para administradores;
- `Minha fila` para administrador cujo perfil também corresponde a um funcionário;
- abertura de tarefa diretamente pelo painel reutilizando o modal existente;
- correção de `todayISO()` para usar `America/Sao_Paulo`;
- nenhum campo, documento ou coleção nova;
- nenhuma alteração em `firebaseConfig`, Authentication, Storage ou regras;
- Preview e deployment de produção da Vercel confirmados com status de sucesso.

Validações realizadas:

- sintaxe JavaScript validada com `node --check`;
- verificação automática de que o bloco do dashboard não contém `setDoc`, `updateDoc`, `addDoc` ou `deleteDoc`;
- teste determinístico da virada UTC x horário de São Paulo;
- revisão do diff do PR;
- automação visual por navegador não pôde ser executada porque o navegador disponível no ambiente bloqueou páginas locais por política administrativa.

### Produção após a Etapa 2

Commit funcional publicado:

`37e53d951af321103a8cb18c62b2fe89aa8e8d6a`

Rollback preservado antes da Etapa 2:

`backup/antes-acesso-compartilhado-2026-08-25`

Alterações funcionais:

- versão visual `1.8.0`;
- login operacional simplificado para uma única conta técnica `alfafiscalto@gmail.com`;
- frontend não mantém mais `allowedUserEmails` nem `userProfiles`;
- funcionários deixaram de depender de e-mail próprio no Firebase;
- qualquer pessoa com a senha do escritório pode selecionar qualquer funcionário pelo card lateral;
- selecionar um nome abre a tela de tarefas já filtrada por esse responsável;
- qualquer pessoa autenticada pode criar serviço para qualquer funcionário ativo e selecionar múltiplos responsáveis;
- `Minha fila` vinculada ao usuário/e-mail foi removida da operação;
- somente a view visível passa a ser renderizada;
- fechamento do seletor ocorre antes da reconstrução do Kanban;
- renderização é adiada para o frame seguinte ao fechar o seletor;
- removidos renders duplicados e reconstruções desnecessárias;
- blur global reduzido e o seletor de funcionário deixou de usar `backdrop-filter`, visando reduzir repaint/INP;
- nenhuma coleção, campo ou documento foi migrado;
- `firebaseConfig`, Storage e regras foram preservados;
- Preview e produção Vercel confirmados com sucesso.

Decisão importante de auditoria:

- `createdBy` e `updatedBy` continuam existindo, mas passam a registrar a conta compartilhada do escritório, não a pessoa física que realizou a ação;
- caso a Alfa queira identificação individual no futuro, isso deverá ser resolvido por uma camada operacional própria, sem voltar obrigatoriamente a criar um usuário Firebase para cada funcionário.

---

# 7. ROADMAP OFICIAL

## ETAPA 0 — Base segura de manutenção

**Status: ✅ CONCLUÍDA em 24/08/2026**

### Objetivo

Criar condições seguras para evoluir o sistema sem perder histórico nem depender da memória de uma conversa.

### Concluído

- baseline funcional identificado;
- arquivo anexado confirmado como correspondente ao `main` da época;
- branch de rollback criada;
- `CONTEXTO_SISTEMA_ALFA.md` criado;
- comentários `ALFA-DEV` adicionados ao código;
- Firebase e estrutura de dados preservados;
- Preview Vercel validado;
- alteração publicada no `main`;
- deployment de produção confirmado.

### Resultado

O projeto agora possui documentação técnica, histórico e rollback antes das próximas mudanças funcionais.

---

## ETAPA 1 — Painel Início / Hoje

**Status: ✅ CONCLUÍDA em 24/08/2026**

### Objetivo

Transformar a primeira tela do sistema em uma central de atenção diária, sem adicionar coleção, documento ou campo ao Firestore.

### Implementado

- novo módulo **🏠 Início**;
- painel aberto automaticamente após login;
- saudação conforme horário do escritório;
- tarefas vencidas;
- tarefas que vencem hoje;
- tarefas que vencem nos próximos 3 dias;
- tarefas de prioridade alta;
- tarefas em andamento;
- lista de atenção ordenada por urgência;
- lista de próximos prazos;
- resumo por responsável para administradores;
- visão `Minha fila` para administrador associado a funcionário;
- botão para abrir a tarefa reutilizando o modal existente;
- botão rápido `+ Novo serviço`;
- correção segura da data operacional para `America/Sao_Paulo`;
- comentários `ALFA-DEV` adicionados nos pontos novos;
- versão visual atualizada para `1.7.0`.

### Segurança confirmada

- nenhuma coleção criada;
- nenhum campo obrigatório criado;
- nenhuma tarefa antiga regravada pela abertura do painel;
- valores de `status` preservados;
- `firebaseConfig` preservado;
- Authentication preservado;
- Storage preservado;
- Kanban existente preservado;
- Clientes, Relatórios e Equipe preservados.

### Publicação

- rollback: `backup/antes-dashboard-inicio-2026-08-24`;
- PR: `#3`;
- commit funcional: `5ac984554f046ba68e62da923e7ea72ff3cb6097`;
- Preview Vercel: sucesso;
- produção Vercel: sucesso.

---

## ETAPA 2 — Acesso compartilhado + desempenho

**Status: ✅ CONCLUÍDA em 25/08/2026**

### Objetivo

Eliminar a necessidade de manter um usuário Firebase por funcionário e reduzir a sensação de travamento nas interações mais frequentes, sem abrir o Firestore ao público.

### Implementado

- uma única conta técnica do escritório no Firebase Authentication;
- login visual solicita apenas a senha do escritório;
- removidos vínculos `e-mail -> funcionário` do frontend;
- todos podem selecionar qualquer funcionário pelo card lateral;
- a seleção abre diretamente as tarefas daquele responsável;
- todos podem criar serviços para qualquer funcionário ativo;
- múltiplos responsáveis continuam suportados;
- funcionários inativos continuam disponíveis apenas no histórico;
- painel e filtros usam o funcionário selecionado, não o e-mail autenticado;
- renderização restrita à view aberta;
- redução de renders duplicados;
- seletor fecha antes do Kanban ser reconstruído;
- render pós-seleção usa `requestAnimationFrame`;
- modal do seletor deixou de usar blur de fundo;
- blur global reduzido de 22px para 14px;
- versão visual `1.8.0`.

### Segurança e compatibilidade

- Firebase Authentication NÃO foi removido;
- Firestore NÃO foi aberto para acesso público;
- `firebaseConfig` preservado;
- coleções `tarefas`, `clientes` e `funcionarios` preservadas;
- campos `employee` e `assignees` preservados;
- usuários antigos do Firebase não foram apagados;
- nenhuma tarefa antiga foi migrada ou regravada apenas por causa da mudança de acesso.

### Auditoria

Com a conta compartilhada, `createdBy` e `updatedBy` identificam a conta técnica do escritório. Eles não identificam qual funcionário estava fisicamente usando o navegador.

### Publicação

- rollback: `backup/antes-acesso-compartilhado-2026-08-25`;
- PR: `#5`;
- commit funcional: `37e53d951af321103a8cb18c62b2fe89aa8e8d6a`;
- Preview Vercel: sucesso;
- produção Vercel: sucesso.

---

## ETAPA 3 — Modo Lista de tarefas

**Status: 🟡 APROVADA COMO PRÓXIMA ETAPA**

### Objetivo

Oferecer uma visualização mais rápida para grande volume de serviços sem remover o Kanban.

### Planejado

Alternância:

```text
Lista | Kanban
```

Colunas sugeridas:

- Cliente;
- Serviço;
- Responsável;
- Prazo;
- Prioridade;
- Status.

### Regra

A Lista deve reutilizar os mesmos objetos `tasks` já carregados.

Não criar uma segunda base de tarefas.

---

## ETAPA 4 — Ficha operacional do cliente

**Status: ⚪ PLANEJADA**

### Objetivo

Transformar o módulo Clientes em uma área operacional, e não apenas cadastral.

### Planejado

Ao selecionar um cliente, mostrar:

- serviços abertos;
- pendentes;
- em andamento;
- concluídos no período;
- vencidos;
- responsáveis;
- histórico disponível pelas tarefas existentes.

### Regra

Primeira versão deve cruzar `clientes` e `tarefas` localmente, sem alterar schema.

---

## ETAPA 5 — Calendário / visão de prazos

**Status: ⚪ PLANEJADA**

### Objetivo

Permitir visualizar a carga de trabalho por prazo.

### Planejado

- visão mensal;
- possibilidade futura de visão semanal;
- tarefas organizadas por `deadline`;
- identificação de vencidas e prioridades;
- acesso da tarefa a partir do calendário.

### Regra

Usar `deadline` existente antes de considerar qualquer campo novo.

---

## ETAPA 6 — Relatórios por pedido ou prazo

**Status: ⚪ PLANEJADA**

### Objetivo

Diferenciar duas análises:

1. tarefas recebidas em determinado mês;
2. tarefas que precisam ser entregues em determinado mês.

### Planejado

Adicionar critério:

```text
Período baseado em:
[ Data do pedido ] [ Prazo limite ]
```

### Regra

- `requestDate` continua válido;
- `deadline` será opção adicional;
- não criar coleção de relatório;
- manter exportação CSV funcionando.

---

## ETAPA 7 — Busca global

**Status: ⚪ PLANEJADA**

### Objetivo

Localizar rapidamente informações sem depender do módulo aberto.

### Planejado

Pesquisar por:

- cliente;
- CNPJ/CPF;
- serviço;
- descrição;
- observação;
- funcionário.

Possível atalho futuro:

`Ctrl + K`

### Regra

A primeira versão deve pesquisar somente os dados já carregados no navegador.

---

## ETAPA 8 — Administração organizada

**Status: ⚪ PLANEJADA**

### Objetivo

Retirar ações administrativas da área operacional principal.

### Planejado

Criar área administrativa para ações como:

- exportar backup;
- importar backup;
- alteração de senha;
- gestão de equipe;
- ferramentas administrativas futuras.

### Atenção

A importação de backup grava no Firestore e deve continuar protegida e claramente diferenciada das funções operacionais. Na versão 1.8.0 a sessão compartilhada ainda possui as ferramentas administrativas existentes; uma separação futura pode usar no máximo uma credencial administrativa adicional, sem voltar ao modelo de um usuário por funcionário.

---

## ETAPA 9 — Anexos / Firebase Storage

**Status: ⚠️ PLANEJADA — EXIGE ANÁLISE ESPECÍFICA**

### Situação atual

O baseline analisado não possui integração funcional com Firebase Storage, apesar de conter:

- `storageBucket` no `firebaseConfig`;
- estilos de anexos.

### Objetivo futuro

Implementar anexos reais para tarefas, se aprovado.

Tipos esperados pelo projeto:

- imagens;
- PDF;
- Word;
- Excel;
- XML;
- TXT.

### Antes de implementar

Confirmar:

- regras atuais do Storage;
- estrutura de pastas;
- relacionamento entre arquivo e tarefa;
- política de exclusão;
- tamanho máximo;
- tratamento de nomes repetidos;
- compatibilidade com eventuais arquivos já existentes no bucket.

### Regra

Não alterar regras do Storage nem apagar arquivos sem autorização expressa.

---

## ETAPA 10 — Limpeza gradual da arquitetura do frontend

**Status: ⚪ PLANEJADA**

### Objetivo

Reduzir risco de manutenção sem fazer uma reescrita geral.

### Pontos planejados

- reduzir CSS duplicado;
- reduzir dependência de `!important`;
- organizar blocos CSS por componente;
- organizar JavaScript por responsabilidade;
- concentrar operações Firestore em funções mais previsíveis;
- padronizar tratamento de erros;
- padronizar loading states;
- revisar overflow e responsividade.

### Regra principal

Essa etapa será incremental.

Não realizar uma grande refatoração estética/arquitetural de uma vez.

Cada limpeza deve provar que não modificou o comportamento esperado.

---

## ETAPA 11 — Gestão avançada

**Status: 🔵 FUTURA — NÃO IMPLEMENTAR AUTOMATICAMENTE**

Possibilidades futuras que podem exigir novos campos ou estruturas:

- histórico detalhado de mudanças de status;
- comentários em tarefas;
- subtarefas/checklists;
- data e hora efetiva de conclusão;
- tarefas recorrentes;
- notificações automáticas;
- SLA;
- tempo médio de execução;
- indicadores de produtividade mais avançados.

Qualquer item desta etapa deve ser discutido antes, pois pode alterar o contrato de dados.

---

# 8. Ordem oficial de execução

A ordem atualmente aprovada é:

| Ordem | Etapa | Status | Risco estimado |
|---|---|---|---|
| 0 | Base segura de manutenção | ✅ Concluída | Muito baixo |
| 1 | Painel Início / Hoje | ✅ Concluída | Muito baixo |
| 2 | Acesso compartilhado + desempenho | ✅ Concluída | Baixo |
| 3 | Modo Lista | 🟡 Próxima | Baixo |
| 4 | Ficha operacional do cliente | ⚪ Planejada | Baixo |
| 5 | Calendário / prazos | ⚪ Planejada | Baixo |
| 6 | Relatórios por pedido/prazo | ⚪ Planejada | Baixo |
| 7 | Busca global | ⚪ Planejada | Baixo |
| 8 | Administração organizada | ⚪ Planejada | Médio |
| 9 | Anexos / Storage | ⚠️ Planejada | Médio |
| 10 | Limpeza gradual da arquitetura | ⚪ Planejada | Médio |
| 11 | Gestão avançada | 🔵 Futura | Avaliar caso a caso |

Essa ordem pode ser alterada pelo usuário, mas nunca silenciosamente pela manutenção.

---

# 9. Critérios gerais de qualidade

Uma versão funcional só deve ser considerada pronta quando, conforme o módulo afetado, forem verificados:

- carregamento da página;
- login;
- carregamento de tarefas;
- criação de tarefa;
- edição de tarefa;
- iniciar tarefa;
- concluir tarefa;
- reabrir tarefa;
- clientes;
- busca;
- filtros;
- relatórios;
- modais;
- sidebar;
- rolagem;
- responsividade;
- permissões administrativas;
- ausência de alteração inesperada no Firestore.

Para anexos, quando a Etapa 9 existir de fato, acrescentar:

- upload;
- leitura/download;
- visualização;
- remoção autorizada;
- tratamento de erro do Storage.

---

# 10. Política de rollback

Antes de cada etapa funcional importante:

1. identificar o commit de produção funcional;
2. criar branch de backup ou outro ponto de restauração claro;
3. registrar esse ponto neste arquivo ou no `CONTEXTO_SISTEMA_ALFA.md`;
4. trabalhar em branch separada;
5. validar Preview Vercel;
6. somente então promover para `main`.

Se a produção apresentar regressão:

- interromper novas mudanças;
- identificar o último commit funcional;
- usar Git/GitHub como mecanismo principal de rollback;
- não restaurar backup JSON de dados para corrigir erro de frontend.

---

# 11. Marcadores técnicos no código

O padrão atual é:

`ALFA-DEV`

Esses comentários devem permanecer apenas em pontos estratégicos, como:

- Firebase;
- autenticação;
- contrato de dados;
- leitura/gravação no Firestore;
- tarefas;
- clientes;
- relatórios;
- anexos;
- filtros;
- modais críticos;
- sidebar/overflow;
- funções que já apresentaram problemas.

Não espalhar comentários em todas as linhas.

Os marcadores antigos citados em versões anteriores deste roteiro (`ALFA-ARCH`, `ALFA-DATA-CONTRACT`, `ALFA-CHANGELOG` e `ALFA-NEXT`) não são mais o padrão principal. A manutenção deve usar `ALFA-DEV` e os dois arquivos Markdown como referência oficial.

---

# 12. Como atualizar este roadmap

Quando uma etapa for concluída:

1. trocar o status da etapa para `✅ CONCLUÍDA`;
2. registrar a data;
3. registrar o commit publicado;
4. registrar a branch de rollback correspondente;
5. resumir o que foi realmente implementado;
6. registrar qualquer decisão diferente do plano original;
7. mover a indicação `PRÓXIMA ETAPA` para a etapa seguinte;
8. garantir que `CONTEXTO_SISTEMA_ALFA.md` também reflita o sistema que passou a existir.

Não apagar o histórico das etapas concluídas.

---

# 13. Instrução curta para futuras manutenções

Antes de alterar o sistema:

1. use somente o `index.html` atual anexado na conversa;
2. leia `CONTEXTO_SISTEMA_ALFA.md`;
3. leia `EVOLUCAO_ALFA_SERVICOS.md`;
4. pesquise `ALFA-DEV` no código;
5. preserve `firebaseConfig` e o contrato do Firestore;
6. crie rollback;
7. altere somente a etapa aprovada;
8. teste em branch/Preview Vercel;
9. atualize a documentação;
10. publique pelo GitHub e confirme a Vercel.

## Próxima ação registrada

**Implementar a ETAPA 3 — Modo Lista de tarefas, preservando o Kanban e reutilizando os mesmos objetos `tasks` já carregados.**
