# Alfa Serviços — roteiro permanente de evolução

> Documento oficial de roadmap e continuidade das evoluções do sistema interno da Alfa Contabilidade.
> Última atualização: 24/08/2026 às 16:56 (America/Sao_Paulo).
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

**Firebase Authentication**

- autenticação por e-mail e senha;
- usuários existentes devem ser preservados;
- problemas de frontend não justificam apagar ou recriar usuários.

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
- usuários e perfis autorizados;
- autenticação por e-mail e senha.

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

**Status: 🟡 APROVADA — PRÓXIMA ETAPA A IMPLEMENTAR**

### Objetivo

Transformar a primeira tela do sistema em uma central de atenção diária, sem adicionar coleção, documento ou campo ao Firestore.

### Escopo aprovado

Criar novo módulo:

**🏠 Início**

O painel deverá utilizar as tarefas já carregadas e mostrar pelo menos:

- tarefas vencidas;
- tarefas que vencem hoje;
- tarefas que vencem nos próximos 3 dias;
- tarefas de prioridade alta;
- tarefas em andamento;
- visão das tarefas do funcionário conectado;
- resumo geral da equipe para administradores.

Exemplo conceitual:

```text
Boa tarde, David

2 vencidas
3 vencem hoje
4 vencem nos próximos 3 dias
2 prioridades altas
5 em andamento
```

### Ajuste técnico incluído nesta etapa

Corrigir o cálculo da data atual.

Função atual:

```javascript
new Date().toISOString().slice(0, 10)
```

Esse cálculo utiliza UTC.

A Etapa 1 deverá utilizar corretamente a data local do navegador/escritório para classificações como:

- vencido;
- vence hoje;
- próximos dias.

Essa correção não deve modificar datas históricas já gravadas.

### Restrições

- não criar nova coleção;
- não criar campos obrigatórios;
- não regravar tarefas antigas;
- não alterar os valores de `status`;
- não alterar `firebaseConfig`;
- não reconstruir o Kanban;
- não implementar calendário ainda;
- não alterar anexos nesta etapa.

### Critérios de aceite

- Início aparece na navegação;
- administrador vê resumo da equipe;
- funcionário comum vê corretamente sua situação;
- tarefa concluída não aparece como vencida;
- múltiplos responsáveis continuam funcionando;
- tarefas vencidas são calculadas corretamente;
- tarefas de hoje são calculadas pela data local;
- Kanban existente continua funcionando;
- Clientes, Relatórios e Equipe continuam funcionando;
- nenhuma gravação adicional no Firestore é gerada apenas ao abrir o painel;
- desktop e telas menores continuam utilizáveis.

---

## ETAPA 2 — Modo Lista de tarefas

**Status: ⚪ PLANEJADA**

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

## ETAPA 3 — Ficha operacional do cliente

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

## ETAPA 4 — Calendário / visão de prazos

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

## ETAPA 5 — Relatórios por pedido ou prazo

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

## ETAPA 6 — Busca global

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

## ETAPA 7 — Administração organizada

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

A importação de backup grava no Firestore e deve continuar protegida e claramente diferenciada das funções operacionais.

---

## ETAPA 8 — Anexos / Firebase Storage

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

## ETAPA 9 — Limpeza gradual da arquitetura do frontend

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

## ETAPA 10 — Gestão avançada

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
| 1 | Painel Início / Hoje | 🟡 Próxima | Muito baixo |
| 2 | Modo Lista | ⚪ Planejada | Baixo |
| 3 | Ficha operacional do cliente | ⚪ Planejada | Baixo |
| 4 | Calendário / prazos | ⚪ Planejada | Baixo |
| 5 | Relatórios por pedido/prazo | ⚪ Planejada | Baixo |
| 6 | Busca global | ⚪ Planejada | Baixo |
| 7 | Administração organizada | ⚪ Planejada | Médio |
| 8 | Anexos / Storage | ⚠️ Planejada | Médio |
| 9 | Limpeza gradual da arquitetura | ⚪ Planejada | Médio |
| 10 | Gestão avançada | 🔵 Futura | Avaliar caso a caso |

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

Para anexos, quando a Etapa 8 existir de fato, acrescentar:

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

**Implementar a ETAPA 1 — Painel Início / Hoje, incluindo correção segura da data local, sem alterar o Firestore.**
