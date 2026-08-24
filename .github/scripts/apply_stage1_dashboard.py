from pathlib import Path

PATH = Path('index.html')
text = PATH.read_text(encoding='utf-8')

if 'ALFA-DEV: PAINEL INÍCIO / HOJE' in text:
    raise SystemExit('Etapa 1 já aplicada; nenhuma alteração feita.')

def replace_once(old, new, label):
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Falha em {label}: esperado 1 anchor, encontrado {count}')
    text = text.replace(old, new, 1)

replace_once('<strong>Versão 1.6.0</strong>', '<strong>Versão 1.7.0</strong>', 'versão visível')
replace_once('versao: "1.6.0",', 'versao: "1.7.0",', 'versão do backup')

css_anchor = '''    /* =========================================================\n       GESTÃO DE EQUIPE — v1.6.0\n'''
css_block = r'''    /* =========================================================
       PAINEL INÍCIO / HOJE — v1.7.0
       ALFA-DEV:
       Camada somente de leitura. Usa tasks/employees já carregados em memória.
       Não criar escrita no Firestore a partir deste painel.
       ========================================================= */
    .home-section {
      padding: 0;
      overflow: hidden;
    }

    .home-hero {
      position: relative;
      overflow: hidden;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      padding: 26px;
      border-bottom: 1px solid var(--border);
      background:
        radial-gradient(circle at 86% 18%, rgba(229,9,20,0.20), transparent 34%),
        rgba(255,255,255,0.018);
    }

    .home-hero::after {
      content: "";
      position: absolute;
      width: 240px;
      height: 240px;
      right: -110px;
      top: -145px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(229,9,20,0.24), transparent 68%);
      pointer-events: none;
    }

    .home-hero-copy {
      position: relative;
      z-index: 1;
      min-width: 0;
    }

    .home-hero h2 {
      margin: 0;
      font-size: clamp(28px, 4vw, 42px);
      line-height: 1;
      letter-spacing: -0.055em;
    }

    .home-hero p {
      margin: 10px 0 0;
      max-width: 760px;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.55;
    }

    .home-hero-actions {
      position: relative;
      z-index: 1;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      justify-content: flex-end;
    }

    .home-kpis {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      border-bottom: 1px solid var(--border);
    }

    .home-kpi {
      min-width: 0;
      padding: 18px 20px;
      border-right: 1px solid var(--border);
      background: rgba(255,255,255,0.018);
    }

    .home-kpi:last-child {
      border-right: 0;
    }

    .home-kpi span {
      display: block;
      color: var(--muted);
      font-size: 11px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .home-kpi strong {
      display: block;
      margin-top: 7px;
      font-size: 30px;
      line-height: 1;
      letter-spacing: -0.055em;
    }

    .home-kpi small {
      display: block;
      margin-top: 7px;
      color: var(--muted-2);
      font-size: 11px;
      line-height: 1.35;
    }

    .home-kpi.danger strong { color: #fca5a5; }
    .home-kpi.today strong { color: #fde68a; }
    .home-kpi.upcoming strong { color: #bfdbfe; }
    .home-kpi.high strong { color: #fecaca; }
    .home-kpi.progress strong { color: #bae6fd; }

    .home-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
      padding: 20px;
    }

    .home-panel {
      min-width: 0;
      overflow: hidden;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      background: rgba(255,255,255,0.028);
    }

    .home-panel-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
      padding: 16px 17px;
      border-bottom: 1px solid var(--border);
      background: rgba(255,255,255,0.025);
    }

    .home-panel-head h3 {
      margin: 0;
      font-size: 16px;
      letter-spacing: -0.025em;
    }

    .home-panel-head p {
      margin: 5px 0 0;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.45;
    }

    .home-list {
      display: grid;
    }

    .home-task-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 14px;
      align-items: center;
      padding: 14px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.075);
    }

    .home-task-row:last-child {
      border-bottom: 0;
    }

    .home-task-main {
      min-width: 0;
    }

    .home-task-main strong {
      display: block;
      overflow-wrap: anywhere;
      font-size: 13px;
      line-height: 1.4;
    }

    .home-task-client {
      display: block;
      margin-top: 4px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      color: var(--muted);
      font-size: 12px;
      font-weight: 600;
    }

    .home-task-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }

    .home-task-meta .pill {
      font-size: 10px;
    }

    .home-task-side {
      display: grid;
      gap: 8px;
      justify-items: end;
    }

    .home-deadline {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 28px;
      padding: 5px 9px;
      border: 1px solid var(--border);
      border-radius: 999px;
      color: var(--muted);
      background: rgba(255,255,255,0.045);
      font-size: 10px;
      font-weight: 900;
      white-space: nowrap;
    }

    .home-deadline.overdue {
      color: #fecaca;
      border-color: rgba(239,68,68,0.42);
      background: rgba(239,68,68,0.13);
    }

    .home-deadline.today {
      color: #fde68a;
      border-color: rgba(245,158,11,0.42);
      background: rgba(245,158,11,0.13);
    }

    .home-deadline.upcoming {
      color: #bfdbfe;
      border-color: rgba(56,189,248,0.32);
      background: rgba(56,189,248,0.10);
    }

    .home-team-panel,
    .home-personal-panel {
      margin: 0 20px 20px;
    }

    .home-team-table-wrap {
      max-height: 360px;
      overflow: auto;
    }

    .home-team-name {
      display: inline-flex;
      align-items: center;
      gap: 9px;
      font-weight: 800;
    }

    .home-empty {
      padding: 24px 16px;
      color: var(--muted-2);
      text-align: center;
      font-size: 12px;
      line-height: 1.5;
    }

    @media (max-width: 1000px) {
      .home-kpis {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .home-kpi {
        border-bottom: 1px solid var(--border);
      }

      .home-grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 720px) {
      .home-hero {
        align-items: flex-start;
        flex-direction: column;
        padding: 20px;
      }

      .home-hero-actions {
        width: 100%;
        justify-content: stretch;
      }

      .home-kpis {
        grid-template-columns: 1fr;
      }

      .home-kpi {
        border-right: 0;
      }

      .home-grid {
        padding: 12px;
      }

      .home-team-panel,
      .home-personal-panel {
        margin: 0 12px 12px;
      }

      .home-task-row {
        grid-template-columns: 1fr;
      }

      .home-task-side {
        justify-items: stretch;
      }

      .home-task-side .icon-btn,
      .home-deadline {
        width: 100%;
      }
    }

'''
replace_once(css_anchor, css_block + css_anchor, 'CSS painel Início')

nav_old = '''      <div class="nav-switch">\n        <button class="employee-btn active" data-view="tasks" id="viewTasksBtn">📋 Tarefas</button>'''
nav_new = '''      <div class="nav-switch">\n        <button class="employee-btn active" data-view="home" id="viewHomeBtn">🏠 Início</button>\n        <button class="employee-btn" data-view="tasks" id="viewTasksBtn">📋 Tarefas</button>'''
replace_once(nav_old, nav_new, 'botão Início')

home_anchor = '''      <div id="systemErrorBox" class="system-error-box"></div>\n\n      <section class="stats">'''
home_html = r'''      <div id="systemErrorBox" class="system-error-box"></div>

      <!-- ALFA-DEV: PAINEL INÍCIO / HOJE — v1.7.0.
      Esta view é SOMENTE DE LEITURA: deriva indicadores das tarefas já carregadas em memória.
      Não adicionar setDoc/updateDoc/addDoc/deleteDoc ao fluxo do painel sem nova aprovação.
      Datas de "hoje" usam America/Sao_Paulo. Histórico: CONTEXTO_SISTEMA_ALFA.md. -->
      <section class="management-section home-section" id="homeSection">
        <div class="home-hero">
          <div class="home-hero-copy">
            <h2 id="homeGreeting">Olá</h2>
            <p id="homeSummaryText">Carregando a situação atual dos serviços...</p>
          </div>
          <div class="home-hero-actions">
            <button class="btn btn-secondary" id="homeOpenTasksBtn" type="button">Ver tarefas</button>
            <button class="btn btn-primary" id="homeNewTaskBtn" type="button">+ Novo serviço</button>
          </div>
        </div>

        <div class="home-kpis" id="homeKpis"></div>

        <div class="home-grid">
          <section class="home-panel">
            <div class="home-panel-head">
              <div>
                <h3 id="homeAttentionTitle">Atenção agora</h3>
                <p>Vencidas, de hoje e prioridades altas ainda abertas.</p>
              </div>
            </div>
            <div class="home-list" id="homeAttentionList"></div>
          </section>

          <section class="home-panel">
            <div class="home-panel-head">
              <div>
                <h3>Próximos 3 dias</h3>
                <p>Serviços com prazo depois de hoje e até os próximos três dias.</p>
              </div>
            </div>
            <div class="home-list" id="homeUpcomingList"></div>
          </section>
        </div>

        <section class="home-panel home-team-panel" id="homeTeamPanel" style="display:none;">
          <div class="home-panel-head">
            <div>
              <h3>Resumo da equipe</h3>
              <p>Serviços abertos, vencidos, de hoje e em andamento por responsável.</p>
            </div>
          </div>
          <div class="home-team-table-wrap">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Responsável</th>
                  <th>Abertos</th>
                  <th>Vencidos</th>
                  <th>Hoje</th>
                  <th>Em andamento</th>
                  <th>Ação</th>
                </tr>
              </thead>
              <tbody id="homeTeamTableBody"></tbody>
            </table>
          </div>
        </section>

        <section class="home-panel home-personal-panel" id="homePersonalPanel" style="display:none;">
          <div class="home-panel-head">
            <div>
              <h3 id="homePersonalTitle">Minha fila</h3>
              <p>Serviços atribuídos diretamente ao usuário conectado.</p>
            </div>
          </div>
          <div class="home-list" id="homePersonalList"></div>
        </section>
      </section>

      <section class="stats">'''
replace_once(home_anchor, home_html, 'HTML painel Início')

dom_old = '''    const employeeSelectOptions = document.getElementById("employeeSelectOptions");\n    const clientsSection = document.getElementById("clientsSection");'''
dom_new = '''    const employeeSelectOptions = document.getElementById("employeeSelectOptions");\n    const homeSection = document.getElementById("homeSection");\n    const clientsSection = document.getElementById("clientsSection");'''
replace_once(dom_old, dom_new, 'referência homeSection')

date_old = '''    function todayISO() {\n      return new Date().toISOString().slice(0, 10);\n    }'''
date_new = r'''    // ALFA-DEV:
    // DATA OPERACIONAL DO ESCRITÓRIO.
    // Comparações de vencimento usam America/Sao_Paulo e não UTC.
    // Isso não regrava nem converte datas já existentes no Firestore.
    const OFFICE_TIME_ZONE = "America/Sao_Paulo";

    function getOfficeDateParts(date = new Date()) {
      const parts = new Intl.DateTimeFormat("en-US", {
        timeZone: OFFICE_TIME_ZONE,
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
      }).formatToParts(date);
      const map = Object.fromEntries(parts.map(part => [part.type, part.value]));
      return { year: map.year, month: map.month, day: map.day };
    }

    function todayISO() {
      const { year, month, day } = getOfficeDateParts();
      return `${year}-${month}-${day}`;
    }

    function addDaysISO(dateString, days) {
      const [year, month, day] = String(dateString || "").split("-").map(Number);
      if (!year || !month || !day) return dateString;
      const date = new Date(Date.UTC(year, month - 1, day));
      date.setUTCDate(date.getUTCDate() + Number(days || 0));
      return date.toISOString().slice(0, 10);
    }

    function calendarDayDiff(fromDate, toDate) {
      const parse = value => {
        const [year, month, day] = String(value || "").split("-").map(Number);
        if (!year || !month || !day) return null;
        return Date.UTC(year, month - 1, day);
      };
      const from = parse(fromDate);
      const to = parse(toDate);
      if (from === null || to === null) return 0;
      return Math.round((to - from) / 86400000);
    }

    function getOfficeHour() {
      const value = new Intl.DateTimeFormat("en-US", {
        timeZone: OFFICE_TIME_ZONE,
        hour: "2-digit",
        hour12: false
      }).format(new Date());
      return Number.parseInt(value, 10) || 0;
    }

    function getOfficeGreeting() {
      const hour = getOfficeHour();
      if (hour < 12) return "Bom dia";
      if (hour < 18) return "Boa tarde";
      return "Boa noite";
    }'''
replace_once(date_old, date_new, 'data local')

view_anchor = '''\n\n    function setView(view) {'''
dashboard_js = r'''

    // ALFA-DEV:
    // VISIBILIDADE COMPARTILHADA ENTRE TAREFAS E PAINEL INÍCIO.
    // Mantém a mesma regra já utilizada: admin vê tudo; funcionário vê tarefas
    // atribuídas a ele e também as que ele próprio criou.
    function isTaskVisibleToCurrentUser(task) {
      const createdByCurrentUser = currentUser?.email
        && normalizeEmail(task.createdBy) === normalizeEmail(currentUser.email);
      return isAdminUser()
        || !currentEmployeeName()
        || taskHasEmployee(task, currentEmployeeName())
        || createdByCurrentUser;
    }

    function getDashboardEmployeeName() {
      if (currentEmployeeName()) return currentEmployeeName();
      const profileName = String(currentUserProfile?.name || "").trim();
      return getEmployeeByName(profileName)?.name || null;
    }

    function getHomeDeadlineMeta(task) {
      const today = todayISO();
      const deadline = task?.deadline || "";
      if (!deadline) return { label: "Sem prazo", className: "" };
      const diff = calendarDayDiff(today, deadline);
      if (task.status !== "concluido" && diff < 0) {
        const days = Math.abs(diff);
        return { label: days === 1 ? "Vencido há 1 dia" : `Vencido há ${days} dias`, className: "overdue" };
      }
      if (task.status !== "concluido" && diff === 0) return { label: "Vence hoje", className: "today" };
      if (task.status !== "concluido" && diff === 1) return { label: "Amanhã", className: "upcoming" };
      if (task.status !== "concluido" && diff > 1 && diff <= 3) return { label: `Em ${diff} dias`, className: "upcoming" };
      return { label: formatDate(deadline), className: "" };
    }

    function homeTaskSort(a, b) {
      const today = todayISO();
      const rank = task => {
        if (isOverdue(task)) return 0;
        if (task.deadline === today && task.status !== "concluido") return 1;
        if (task.priority === "alta" && task.status !== "concluido") return 2;
        if (task.deadline) return 3;
        return 4;
      };
      const rankDiff = rank(a) - rank(b);
      if (rankDiff) return rankDiff;
      const deadlineDiff = String(a.deadline || "9999-12-31").localeCompare(String(b.deadline || "9999-12-31"));
      if (deadlineDiff) return deadlineDiff;
      const priorityRank = { alta: 0, media: 1, baixa: 2 };
      return (priorityRank[a.priority] ?? 9) - (priorityRank[b.priority] ?? 9);
    }

    function renderHomeTaskRows(targetId, rows, emptyMessage) {
      const container = document.getElementById(targetId);
      if (!container) return;
      const limited = [...rows].sort(homeTaskSort).slice(0, 8);
      if (!limited.length) {
        container.innerHTML = `<div class="home-empty">${escapeHTML(emptyMessage)}</div>`;
        return;
      }
      container.innerHTML = limited.map(task => {
        const deadlineMeta = getHomeDeadlineMeta(task);
        return `
          <div class="home-task-row">
            <div class="home-task-main">
              <strong>${escapeHTML(task.serviceType || "Serviço sem título")}</strong>
              <span class="home-task-client">${escapeHTML(task.clientAlias || task.clientName || "Sem cliente informado")}</span>
              <div class="home-task-meta">
                <span class="pill">👥 ${escapeHTML(getTaskAssigneeText(task))}</span>
                <span class="pill priority-${escapeHTML(task.priority || "media")}">${escapeHTML(priorityLabels[task.priority] || "Média")}</span>
                <span class="pill">📌 ${escapeHTML(statusLabels[task.status] || task.status || "Pendente")}</span>
              </div>
            </div>
            <div class="home-task-side">
              <span class="home-deadline ${deadlineMeta.className}">${escapeHTML(deadlineMeta.label)}</span>
              <button class="icon-btn" type="button" data-home-task="${escapeHTML(task.id || "")}">Abrir</button>
            </div>
          </div>`;
      }).join("");
    }

    function renderHomeTeamSummary() {
      const panel = document.getElementById("homeTeamPanel");
      const tbody = document.getElementById("homeTeamTableBody");
      if (!panel || !tbody) return;

      if (!isAdminUser()) {
        panel.style.display = "none";
        tbody.innerHTML = "";
        return;
      }

      panel.style.display = "block";
      const today = todayISO();
      const rows = employees.map(employee => {
        const employeeTasks = tasks.filter(task => taskHasEmployee(task, employee.name));
        const openTasks = employeeTasks.filter(task => task.status !== "concluido");
        return {
          employee,
          open: openTasks.length,
          overdue: openTasks.filter(isOverdue).length,
          today: openTasks.filter(task => task.deadline === today).length,
          progress: openTasks.filter(task => task.status === "andamento").length
        };
      }).filter(row => row.employee.active !== false || row.open > 0)
        .sort((a, b) => b.overdue - a.overdue || b.today - a.today || b.open - a.open || a.employee.name.localeCompare(b.employee.name, "pt-BR"));

      tbody.innerHTML = rows.map(row => `
        <tr>
          <td>
            <span class="home-team-name">
              <span class="dot" style="color:${escapeHTML(row.employee.color)}"></span>
              ${escapeHTML(row.employee.name)}
            </span>
          </td>
          <td><strong>${row.open}</strong></td>
          <td>${row.overdue ? `<span class="pill visual-vencido">${row.overdue}</span>` : "0"}</td>
          <td>${row.today ? `<span class="pill visual-hoje">${row.today}</span>` : "0"}</td>
          <td>${row.progress}</td>
          <td><button class="icon-btn" type="button" data-home-employee="${escapeHTML(row.employee.name)}">Ver tarefas</button></td>
        </tr>
      `).join("") || `<tr><td colspan="6">Nenhum funcionário com serviços para exibir.</td></tr>`;
    }

    function renderHomePersonalQueue() {
      const panel = document.getElementById("homePersonalPanel");
      const title = document.getElementById("homePersonalTitle");
      if (!panel || !title) return;

      const employeeName = getDashboardEmployeeName();
      if (!isAdminUser() || !employeeName) {
        panel.style.display = "none";
        renderHomeTaskRows("homePersonalList", [], "");
        return;
      }

      panel.style.display = "block";
      title.textContent = `Minha fila — ${employeeName}`;
      const personalOpen = tasks.filter(task => taskHasEmployee(task, employeeName) && task.status !== "concluido");
      renderHomeTaskRows("homePersonalList", personalOpen, "Nenhum serviço aberto atribuído diretamente a você.");
    }

    function renderHomeDashboard() {
      if (!homeSection) return;

      const today = todayISO();
      const nextThreeDays = addDaysISO(today, 3);
      const visibleTasks = tasks.filter(isTaskVisibleToCurrentUser);
      const openTasks = visibleTasks.filter(task => task.status !== "concluido");
      const overdue = openTasks.filter(isOverdue);
      const dueToday = openTasks.filter(task => task.deadline === today);
      const upcoming = openTasks.filter(task => task.deadline > today && task.deadline <= nextThreeDays);
      const highPriority = openTasks.filter(task => task.priority === "alta");
      const inProgress = openTasks.filter(task => task.status === "andamento");

      const greetingName = currentUserProfile?.name || currentUser?.email || "equipe";
      const greeting = document.getElementById("homeGreeting");
      const summary = document.getElementById("homeSummaryText");
      const attentionTitle = document.getElementById("homeAttentionTitle");
      if (greeting) greeting.textContent = `${getOfficeGreeting()}, ${greetingName}`;
      if (summary) {
        const subject = isAdminUser() ? "A equipe" : "Você";
        summary.textContent = `${subject} tem ${overdue.length} ${overdue.length === 1 ? "tarefa vencida" : "tarefas vencidas"}, ${dueToday.length} para hoje e ${inProgress.length} em andamento.`;
      }
      if (attentionTitle) attentionTitle.textContent = isAdminUser() ? "Atenção da equipe" : "Minha fila de atenção";

      const kpis = document.getElementById("homeKpis");
      if (kpis) {
        const items = [
          { label: "Vencidas", value: overdue.length, hint: "prazo já passou", tone: "danger" },
          { label: "Vencem hoje", value: dueToday.length, hint: "prioridade do dia", tone: "today" },
          { label: "Próximos 3 dias", value: upcoming.length, hint: "depois de hoje", tone: "upcoming" },
          { label: "Alta prioridade", value: highPriority.length, hint: "ainda abertas", tone: "high" },
          { label: "Em andamento", value: inProgress.length, hint: "serviços iniciados", tone: "progress" }
        ];
        kpis.innerHTML = items.map(item => `
          <div class="home-kpi ${item.tone}">
            <span>${escapeHTML(item.label)}</span>
            <strong>${item.value}</strong>
            <small>${escapeHTML(item.hint)}</small>
          </div>`).join("");
      }

      const attention = openTasks.filter(task => isOverdue(task) || task.deadline === today || task.priority === "alta");
      renderHomeTaskRows("homeAttentionList", attention, "Nenhuma tarefa crítica neste momento.");
      renderHomeTaskRows("homeUpcomingList", upcoming, "Nenhum prazo nos próximos três dias.");
      renderHomeTeamSummary();
      renderHomePersonalQueue();
    }

    function handleHomeAction(event) {
      const taskButton = event.target.closest("[data-home-task]");
      if (taskButton) {
        const task = tasks.find(item => item.id === taskButton.dataset.homeTask);
        if (task) openModal(task);
        return;
      }

      const employeeButton = event.target.closest("[data-home-employee]");
      if (employeeButton && isAdminUser()) {
        selectEmployee(employeeButton.dataset.homeEmployee);
        setView("tasks");
      }
    }
'''
replace_once(view_anchor, dashboard_js + view_anchor, 'JavaScript painel Início')

setview_old = r'''      document.querySelectorAll("[data-view]").forEach(btn => btn.classList.toggle("active", btn.dataset.view === view));
      taskSections.forEach(section => { if (section) section.style.display = view === "tasks" ? "" : "none"; });
      clientsSection.classList.toggle("active", view === "clients");
      employeesSection.classList.toggle("active", view === "employees");
      reportsSection.classList.toggle("active", view === "reports");
      if (view === "clients") renderClients();
      if (view === "employees") renderEmployeesManagement();
      if (view === "reports") generateReport();'''
setview_new = r'''      document.querySelectorAll("[data-view]").forEach(btn => btn.classList.toggle("active", btn.dataset.view === view));
      taskSections.forEach(section => { if (section) section.style.display = view === "tasks" ? "" : "none"; });
      homeSection.classList.toggle("active", view === "home");
      clientsSection.classList.toggle("active", view === "clients");
      employeesSection.classList.toggle("active", view === "employees");
      reportsSection.classList.toggle("active", view === "reports");
      if (view === "home") renderHomeDashboard();
      if (view === "clients") renderClients();
      if (view === "employees") renderEmployeesManagement();
      if (view === "reports") generateReport();'''
replace_once(setview_old, setview_new, 'setView home')

filter_old = r'''        const assigneeText = getTaskAssigneeText(task);
        const createdByCurrentUser = currentUser?.email && normalizeEmail(task.createdBy) === normalizeEmail(currentUser.email);
        const byLoggedUser = isAdminUser() || !currentEmployeeName() || taskHasEmployee(task, currentEmployeeName()) || createdByCurrentUser;
        const byEmployee = selectedEmployee === "todos" || taskHasEmployee(task, selectedEmployee) || (!isAdminUser() && createdByCurrentUser);'''
filter_new = r'''        const assigneeText = getTaskAssigneeText(task);
        const createdByCurrentUser = currentUser?.email && normalizeEmail(task.createdBy) === normalizeEmail(currentUser.email);
        const byLoggedUser = isTaskVisibleToCurrentUser(task);
        const byEmployee = selectedEmployee === "todos" || taskHasEmployee(task, selectedEmployee) || (!isAdminUser() && createdByCurrentUser);'''
replace_once(filter_old, filter_new, 'visibilidade compartilhada')

render_old = r'''      renderColumn("listPendente", filtered.filter(task => task.status === "pendente"));
      renderColumn("listAndamento", filtered.filter(task => task.status === "andamento"));
      renderColumn("listConcluido", filtered.filter(task => task.status === "concluido"));
    }'''
render_new = r'''      renderColumn("listPendente", filtered.filter(task => task.status === "pendente"));
      renderColumn("listAndamento", filtered.filter(task => task.status === "andamento"));
      renderColumn("listConcluido", filtered.filter(task => task.status === "concluido"));
      renderHomeDashboard();
    }'''
replace_once(render_old, render_new, 'render dashboard')

showapp_old = r'''      loginScreen.style.display = "none";
      appShell.classList.add("visible");
      setConnection("online", "Conectado ao Firebase");
      listenEmployees();'''
showapp_new = r'''      loginScreen.style.display = "none";
      appShell.classList.add("visible");
      setConnection("online", "Conectado ao Firebase");
      setView("home");
      listenEmployees();'''
replace_once(showapp_old, showapp_new, 'home default pós-login')

events_old = r'''    document.getElementById("viewTasksBtn").addEventListener("click", () => setView("tasks"));
    document.getElementById("viewClientsBtn").addEventListener("click", () => setView("clients"));'''
events_new = r'''    document.getElementById("viewHomeBtn").addEventListener("click", () => setView("home"));
    document.getElementById("viewTasksBtn").addEventListener("click", () => setView("tasks"));
    document.getElementById("viewClientsBtn").addEventListener("click", () => setView("clients"));'''
replace_once(events_old, events_new, 'listener Início')

home_events_anchor = r'''    document.getElementById("viewEmployeesBtn").addEventListener("click", () => setView("employees"));
    document.getElementById("openEmployeeModalBtn").addEventListener("click", () => openEmployeeManagementModal());'''
home_events_new = r'''    document.getElementById("viewEmployeesBtn").addEventListener("click", () => setView("employees"));
    document.getElementById("homeOpenTasksBtn").addEventListener("click", () => setView("tasks"));
    document.getElementById("homeNewTaskBtn").addEventListener("click", () => openModal());
    homeSection.addEventListener("click", handleHomeAction);
    document.getElementById("openEmployeeModalBtn").addEventListener("click", () => openEmployeeManagementModal());'''
replace_once(home_events_anchor, home_events_new, 'eventos dashboard')

PATH.write_text(text, encoding='utf-8')
print('Etapa 1 aplicada com sucesso.')
