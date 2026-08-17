from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"[{label}] expected exactly 1 match, found {count}")
    text = text.replace(old, new, 1)


# Version badge
replace_once(
    '<strong>Versão 1.5.3</strong>',
    '<strong>Versão 1.6.0</strong>',
    'version badge',
)

# Employee management styles (isolated; does not alter existing task/client styles).
css_anchor = "\n  </style>"
employee_css = r'''

    /* =========================================================
       GESTÃO DE EQUIPE — v1.6.0
       Camada visual isolada da estrutura de tarefas/clientes.
       ========================================================= */
    .team-summary {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }

    .team-summary-card {
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 14px;
      background: rgba(255,255,255,0.045);
    }

    .team-summary-card span {
      display: block;
      color: var(--muted);
      font-size: 11px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .team-summary-card strong {
      display: block;
      margin-top: 7px;
      font-size: 26px;
      letter-spacing: -0.05em;
    }

    .team-table-wrap {
      max-height: 540px;
      overflow: auto;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      background: rgba(255,255,255,0.035);
    }

    .employee-status {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 5px 9px;
      border-radius: 999px;
      border: 1px solid var(--border);
      font-size: 11px;
      font-weight: 900;
    }

    .employee-status.active {
      color: #bbf7d0;
      border-color: rgba(34,197,94,0.36);
      background: rgba(34,197,94,0.12);
    }

    .employee-status.inactive {
      color: #cbd5e1;
      border-color: rgba(148,163,184,0.26);
      background: rgba(148,163,184,0.09);
    }

    .employee-color-chip {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
    }

    .employee-color-preview {
      width: 24px;
      height: 24px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.22);
      box-shadow: 0 0 20px color-mix(in srgb, currentColor 32%, transparent);
      background: currentColor;
    }

    .employee-form-grid {
      display: grid;
      grid-template-columns: 1fr 150px;
      gap: 12px;
      align-items: end;
    }

    .employee-active-toggle {
      display: flex;
      align-items: center;
      gap: 10px;
      min-height: 48px;
      padding: 12px 13px;
      border: 1px solid var(--border);
      border-radius: 16px;
      background: rgba(255,255,255,0.055);
      color: var(--text);
      font-size: 13px;
      font-weight: 800;
      text-transform: none;
      letter-spacing: normal;
    }

    .employee-active-toggle input {
      width: 17px;
      height: 17px;
      accent-color: var(--red);
    }

    .team-note {
      margin-top: 14px;
      padding: 12px 14px;
      border: 1px solid rgba(56,189,248,0.22);
      border-radius: 16px;
      background: rgba(56,189,248,0.07);
      color: #bae6fd;
      font-size: 12px;
      line-height: 1.5;
    }

    @media (max-width: 720px) {
      .team-summary,
      .employee-form-grid {
        grid-template-columns: 1fr;
      }
    }
'''
replace_once(css_anchor, employee_css + css_anchor, 'employee css')

# Navigation: add a dedicated Team module without changing existing module ids.
nav_old = '''        <button class="employee-btn" data-view="reports" id="viewReportsBtn">📊 Relatórios</button>'''
nav_new = nav_old + '''\n        <button class="employee-btn" data-view="employees" id="viewEmployeesBtn">👥 Equipe</button>'''
replace_once(nav_old, nav_new, 'team nav button')

# Team management section. This is admin-only at runtime and uses a new Firestore collection.
reports_anchor = '''      <section class="management-section" id="reportsSection">'''
employees_section = r'''      <section class="management-section" id="employeesSection">
        <div class="section-head">
          <div>
            <h2>Equipe e responsáveis</h2>
            <p>Cadastre novas pessoas, ajuste a cor de identificação e inative quem saiu sem apagar o histórico das tarefas.</p>
          </div>
          <button class="btn btn-primary" id="openEmployeeModalBtn" type="button">+ Novo funcionário</button>
        </div>

        <div class="team-summary" id="employeeManagementKpis"></div>

        <div class="team-table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>Funcionário</th>
                <th>Situação</th>
                <th>Serviços abertos</th>
                <th>Identificação</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody id="employeesTableBody"></tbody>
          </table>
        </div>

        <div class="team-note">
          <strong>Histórico protegido:</strong> ao inativar uma pessoa, as tarefas antigas continuam vinculadas ao mesmo nome e permanecem disponíveis em filtros e relatórios. A inativação apenas impede novas atribuições.
        </div>
      </section>

'''
replace_once(reports_anchor, employees_section + reports_anchor, 'employees section')

# Employee modal before existing client import modal.
client_import_anchor = '''  <div class="modal" id="clientImportModal">'''
employee_modal = r'''  <div class="modal" id="employeeManagementModal">
    <div class="modal-card" style="width: min(620px, 100%);">
      <div class="modal-header">
        <h3 id="employeeManagementModalTitle">Novo funcionário</h3>
        <button class="icon-btn" id="closeEmployeeManagementModalBtn" type="button">✕</button>
      </div>

      <form id="employeeManagementForm">
        <input type="hidden" id="employeeManagementId" />
        <div class="employee-form-grid">
          <div class="field">
            <label for="employeeManagementName">Nome</label>
            <input id="employeeManagementName" placeholder="Ex.: Mariana" required />
            <small class="doc-hint" id="employeeNameHint">Depois do cadastro, o nome fica protegido para não quebrar o vínculo com tarefas antigas.</small>
          </div>
          <div class="field">
            <label for="employeeManagementColor">Cor</label>
            <input id="employeeManagementColor" type="color" value="#38bdf8" style="height: 48px; padding: 6px;" />
          </div>
          <div class="field full">
            <label class="employee-active-toggle">
              <input type="checkbox" id="employeeManagementActive" checked />
              Funcionário ativo e disponível para novas tarefas
            </label>
          </div>
        </div>

        <div class="actions" style="margin-top: 16px;">
          <button type="button" class="btn btn-ghost" id="cancelEmployeeManagementBtn">Cancelar</button>
          <button type="submit" class="btn btn-primary">Salvar funcionário</button>
        </div>
      </form>
    </div>
  </div>

'''
replace_once(client_import_anchor, employee_modal + client_import_anchor, 'employee modal')

# Replace hard-coded roster with a compatibility seed + runtime Firestore roster.
employees_old = '''    const employees = [
      { name: "Henrique", color: "#ef4444" },
      { name: "Rebeca", color: "#ff4fa3" },
      { name: "David", color: "#38bdf8" },
      { name: "Amanda", color: "#a855f7" },
      { name: "Flavia", color: "#22c55e" },
      { name: "Joyce", color: "#f59e0b" },
      { name: "Julyana", color: "#14b8a6" }
    ];'''
employees_new = '''    const defaultEmployees = [
      { id: "henrique", name: "Henrique", color: "#ef4444", active: true },
      { id: "rebeca", name: "Rebeca", color: "#ff4fa3", active: false },
      { id: "david", name: "David", color: "#38bdf8", active: true },
      { id: "amanda", name: "Amanda", color: "#a855f7", active: true },
      { id: "flavia", name: "Flavia", color: "#22c55e", active: true },
      { id: "joyce", name: "Joyce", color: "#f59e0b", active: true },
      { id: "julyana", name: "Julyana", color: "#14b8a6", active: true },
      { id: "laila", name: "Laila", color: "#f97316", active: true },
      { id: "mariana", name: "Mariana", color: "#06b6d4", active: true }
    ];

    // A lista acima é somente uma base de compatibilidade. Alterações feitas em
    // "Equipe" são salvas na coleção "funcionarios" do Firestore e sobrescrevem
    // os dados correspondentes sem mudar o formato das tarefas existentes.
    let employees = defaultEmployees.map(employee => ({ ...employee }));'''
replace_once(employees_old, employees_new, 'employee seed')

# Rebeca no longer has front-end authorization. Historical task data remains untouched.
replace_once('      "rebcaravila@gmail.com",\n', '', 'remove rebeca allowed email')
replace_once('      "rebcaravila@gmail.com": { name: "Rebeca", role: "Funcionária", employee: "Rebeca" },\n', '', 'remove rebeca user profile')

# Runtime state for employee subscription/editor.
replace_once(
    '    let unsubscribeClients = null;\n',
    '    let unsubscribeClients = null;\n    let unsubscribeEmployees = null;\n',
    'employee unsubscribe state',
)
replace_once(
    '    let editingClientId = null;\n',
    '    let editingClientId = null;\n    let editingEmployeeId = null;\n',
    'employee edit state',
)

# DOM references.
replace_once(
    '    const clientsSection = document.getElementById("clientsSection");\n    const reportsSection = document.getElementById("reportsSection");',
    '    const clientsSection = document.getElementById("clientsSection");\n    const employeesSection = document.getElementById("employeesSection");\n    const reportsSection = document.getElementById("reportsSection");',
    'employee dom reference',
)

# View routing.
set_view_old = '''    function setView(view) {
      document.querySelectorAll("[data-view]").forEach(btn => btn.classList.toggle("active", btn.dataset.view === view));
      taskSections.forEach(section => { if (section) section.style.display = view === "tasks" ? "" : "none"; });
      clientsSection.classList.toggle("active", view === "clients");
      reportsSection.classList.toggle("active", view === "reports");
      if (view === "clients") renderClients();
      if (view === "reports") generateReport();
    }'''
set_view_new = '''    function setView(view) {
      if (view === "employees" && !isAdminUser()) {
        showToast("A gestão da equipe é exclusiva do administrador.");
        view = "tasks";
      }
      document.querySelectorAll("[data-view]").forEach(btn => btn.classList.toggle("active", btn.dataset.view === view));
      taskSections.forEach(section => { if (section) section.style.display = view === "tasks" ? "" : "none"; });
      clientsSection.classList.toggle("active", view === "clients");
      employeesSection.classList.toggle("active", view === "employees");
      reportsSection.classList.toggle("active", view === "reports");
      if (view === "clients") renderClients();
      if (view === "employees") renderEmployeesManagement();
      if (view === "reports") generateReport();
    }'''
replace_once(set_view_old, set_view_new, 'view routing')

# Backup now includes employee configuration while keeping old backup fields compatible.
replace_once(
    '        versao: "1.5.3",',
    '        versao: "1.6.0",',
    'backup version',
)
replace_once(
    '        totalClientes: clients.length,\n        tarefas: tasks,\n        clientes: clients',
    '        totalClientes: clients.length,\n        totalFuncionarios: employees.length,\n        tarefas: tasks,\n        clientes: clients,\n        funcionarios: employees',
    'backup employees export',
)
replace_once(
    '      showToast("Backup exportado em JSON com tarefas e clientes.");',
    '      showToast("Backup exportado em JSON com tarefas, clientes e equipe.");',
    'backup toast',
)
replace_once(
    '      const backupClients = Array.isArray(backup.clientes) ? backup.clientes : [];\n      if (!backupTasks.length && !backupClients.length) {\n        showToast("O backup não possui tarefas nem clientes para importar.");',
    '      const backupClients = Array.isArray(backup.clientes) ? backup.clientes : [];\n      const backupEmployees = Array.isArray(backup.funcionarios) ? backup.funcionarios : [];\n      if (!backupTasks.length && !backupClients.length && !backupEmployees.length) {\n        showToast("O backup não possui tarefas, clientes nem funcionários para importar.");',
    'backup employees parse',
)
replace_once(
    '      const confirmImport = confirm(`Importar backup com ${backupTasks.length} tarefa(s) e ${backupClients.length} cliente(s)? Registros com o mesmo ID serão atualizados.`);',
    '      const confirmImport = confirm(`Importar backup com ${backupTasks.length} tarefa(s), ${backupClients.length} cliente(s) e ${backupEmployees.length} funcionário(s)? Registros com o mesmo ID serão atualizados.`);',
    'backup confirm',
)
backup_write_old = '''        for (const item of backupClients) {
          const cleaned = cleanBackupRecord(item, currentUser?.email);
          if (item.id) await setDoc(doc(db, "clientes", item.id), cleaned, { merge: true });
          else await addDoc(collection(db, "clientes"), cleaned);
        }
        showToast("Backup importado com sucesso.");'''
backup_write_new = '''        for (const item of backupClients) {
          const cleaned = cleanBackupRecord(item, currentUser?.email);
          if (item.id) await setDoc(doc(db, "clientes", item.id), cleaned, { merge: true });
          else await addDoc(collection(db, "clientes"), cleaned);
        }
        for (const item of backupEmployees) {
          const name = String(item.name || "").trim();
          if (!name) continue;
          const employeeId = item.id || employeeSlug(name);
          await setDoc(doc(db, "funcionarios", employeeId), {
            name,
            color: item.color || "#64748b",
            active: item.active !== false,
            restoredAt: serverTimestamp(),
            restoredBy: currentUser?.email || null
          }, { merge: true });
        }
        showToast("Backup importado com sucesso.");'''
replace_once(backup_write_old, backup_write_new, 'backup employees write')

# Insert employee compatibility/CRUD helpers before the existing employee selector helpers.
employee_helpers_anchor = '''    function getEmployeeColor(employeeName) {'''
employee_helpers = r'''    function employeeSlug(value) {
      return String(value || "")
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "")
        .slice(0, 60);
    }

    function normalizeEmployeeRecord(employee, fallbackId = "") {
      const name = String(employee?.name || "").trim();
      return {
        id: String(employee?.id || fallbackId || employeeSlug(name)).trim(),
        name,
        color: /^#[0-9a-f]{6}$/i.test(String(employee?.color || "")) ? employee.color : "#64748b",
        active: employee?.active !== false,
        source: employee?.source || "firebase"
      };
    }

    function mergeEmployeeRoster(firebaseEmployees = []) {
      const roster = new Map();
      defaultEmployees.forEach(employee => {
        const normalized = normalizeEmployeeRecord({ ...employee, source: "default" }, employee.id);
        roster.set(normalized.name.toLocaleLowerCase("pt-BR"), normalized);
      });
      firebaseEmployees.forEach(employee => {
        const normalized = normalizeEmployeeRecord(employee, employee.id);
        if (!normalized.name) return;
        roster.set(normalized.name.toLocaleLowerCase("pt-BR"), normalized);
      });
      return Array.from(roster.values()).sort((a, b) => {
        if (a.active !== b.active) return a.active ? -1 : 1;
        return a.name.localeCompare(b.name, "pt-BR");
      });
    }

    function getActiveEmployees() {
      return employees.filter(employee => employee.active !== false);
    }

    function getEmployeeByName(employeeName) {
      const target = String(employeeName || "").trim().toLocaleLowerCase("pt-BR");
      return employees.find(employee => employee.name.toLocaleLowerCase("pt-BR") === target) || null;
    }

    function enrichEmployeesFromTasks() {
      let changed = false;
      tasks.forEach(task => {
        const rawNames = Array.isArray(task?.assignees) && task.assignees.length
          ? task.assignees
          : (task?.employee ? [task.employee] : []);
        rawNames.forEach(rawName => {
          const name = String(rawName || "").trim();
          if (!name || getEmployeeByName(name)) return;
          employees.push({
            id: `historico-${employeeSlug(name) || "sem-id"}`,
            name,
            color: "#64748b",
            active: false,
            source: "historical"
          });
          changed = true;
        });
      });
      if (changed) {
        employees.sort((a, b) => {
          if (a.active !== b.active) return a.active ? -1 : 1;
          return a.name.localeCompare(b.name, "pt-BR");
        });
      }
      return changed;
    }

    function renderEmployeesManagement() {
      const tbody = document.getElementById("employeesTableBody");
      const kpis = document.getElementById("employeeManagementKpis");
      if (!tbody || !kpis) return;

      const activeEmployees = getActiveEmployees();
      const inactiveEmployees = employees.filter(employee => employee.active === false);
      const openTasks = tasks.filter(task => task.status !== "concluido").length;

      kpis.innerHTML = [
        ["Ativos", activeEmployees.length],
        ["Inativos / histórico", inactiveEmployees.length],
        ["Serviços abertos", openTasks]
      ].map(([label, value]) => `<div class="team-summary-card"><span>${label}</span><strong>${value}</strong></div>`).join("");

      tbody.innerHTML = employees.map(employee => {
        const openCount = getEmployeeOpenCount(employee.name);
        const inactive = employee.active === false;
        const historicalOnly = employee.source === "historical";
        return `
          <tr>
            <td>
              <strong>${escapeHTML(employee.name)}</strong>
              ${historicalOnly ? `<br><span style="color: var(--muted-2); font-size: 11px;">Detectado em tarefa antiga</span>` : ""}
            </td>
            <td><span class="employee-status ${inactive ? "inactive" : "active"}">${inactive ? "Inativo" : "Ativo"}</span></td>
            <td><strong>${openCount}</strong></td>
            <td>
              <span class="employee-color-chip">
                <span class="employee-color-preview" style="color:${escapeHTML(employee.color)}"></span>
                ${escapeHTML(employee.color)}
              </span>
            </td>
            <td>
              <div class="table-actions">
                <button class="icon-btn" data-employee-action="edit" data-id="${escapeHTML(employee.id)}">Editar</button>
                <button class="icon-btn ${inactive ? "btn-start" : "danger"}" data-employee-action="toggle" data-id="${escapeHTML(employee.id)}" ${historicalOnly ? "disabled" : ""}>${inactive ? "Reativar" : "Inativar"}</button>
              </div>
            </td>
          </tr>
        `;
      }).join("") || `<tr><td colspan="5">Nenhum funcionário cadastrado.</td></tr>`;
    }

    function openEmployeeManagementModal(employee = null) {
      if (!isAdminUser()) {
        showToast("A gestão da equipe é exclusiva do administrador.");
        return;
      }
      editingEmployeeId = employee?.id || null;
      const modal = document.getElementById("employeeManagementModal");
      const nameInput = document.getElementById("employeeManagementName");
      document.getElementById("employeeManagementModalTitle").textContent = employee ? "Editar funcionário" : "Novo funcionário";
      document.getElementById("employeeManagementId").value = employee?.id || "";
      nameInput.value = employee?.name || "";
      nameInput.disabled = Boolean(employee);
      document.getElementById("employeeNameHint").textContent = employee
        ? "O nome fica bloqueado na edição para preservar os vínculos com tarefas e relatórios antigos."
        : "Cadastre o nome como ele deve aparecer nas tarefas. Depois do cadastro, ele fica protegido.";
      document.getElementById("employeeManagementColor").value = employee?.color || "#38bdf8";
      document.getElementById("employeeManagementActive").checked = employee ? employee.active !== false : true;
      modal.classList.add("open");
      document.body.classList.add("modal-is-open");
    }

    function closeEmployeeManagementModal() {
      const modal = document.getElementById("employeeManagementModal");
      modal.classList.remove("open");
      document.body.classList.remove("modal-is-open");
      document.getElementById("employeeManagementForm").reset();
      document.getElementById("employeeManagementName").disabled = false;
      editingEmployeeId = null;
    }

    async function saveEmployeeManagement(event) {
      event.preventDefault();
      if (!isAdminUser() || !firebaseReady || !currentUser) {
        showToast("Somente o administrador conectado pode alterar a equipe.");
        return;
      }

      const nameInput = document.getElementById("employeeManagementName");
      const name = nameInput.value.trim();
      const color = document.getElementById("employeeManagementColor").value;
      const active = document.getElementById("employeeManagementActive").checked;
      if (!name) {
        showToast("Informe o nome do funcionário.");
        return;
      }

      const existingByName = getEmployeeByName(name);
      if (!editingEmployeeId && existingByName) {
        showToast("Já existe um funcionário com esse nome. Edite o cadastro existente.");
        return;
      }

      const employeeId = editingEmployeeId || employeeSlug(name) || doc(collection(db, "funcionarios")).id;
      const submitButton = document.querySelector('#employeeManagementForm button[type="submit"]');
      const originalText = submitButton?.textContent || "Salvar funcionário";

      try {
        if (submitButton) {
          submitButton.disabled = true;
          submitButton.textContent = "Salvando...";
        }
        await setDoc(doc(db, "funcionarios", employeeId), {
          name,
          color,
          active,
          updatedAt: serverTimestamp(),
          updatedBy: currentUser.email,
          ...(editingEmployeeId ? {} : { createdAt: serverTimestamp(), createdBy: currentUser.email })
        }, { merge: true });
        closeEmployeeManagementModal();
        showToast(editingEmployeeId ? "Funcionário atualizado." : "Funcionário adicionado à equipe.");
      } catch (error) {
        console.error(error);
        showToast(error?.code === "permission-denied"
          ? "O Firestore bloqueou a coleção funcionarios. As tarefas continuam funcionando; é necessário liberar essa coleção nas regras do Firebase."
          : (error?.message || "Não foi possível salvar o funcionário."));
      } finally {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.textContent = originalText;
        }
      }
    }

    async function toggleEmployeeActive(employee) {
      if (!employee || employee.source === "historical") return;
      if (!isAdminUser() || !firebaseReady || !currentUser) {
        showToast("Somente o administrador conectado pode alterar a equipe.");
        return;
      }
      const nextActive = employee.active === false;
      const action = nextActive ? "reativar" : "inativar";
      if (!confirm(`Deseja ${action} ${employee.name}? As tarefas antigas não serão apagadas.`)) return;
      try {
        await setDoc(doc(db, "funcionarios", employee.id || employeeSlug(employee.name)), {
          name: employee.name,
          color: employee.color,
          active: nextActive,
          updatedAt: serverTimestamp(),
          updatedBy: currentUser.email
        }, { merge: true });
        showToast(`${employee.name} ${nextActive ? "reativado(a)" : "inativado(a)"} com sucesso.`);
      } catch (error) {
        console.error(error);
        showToast(error?.code === "permission-denied"
          ? "O Firestore bloqueou a coleção funcionarios. Nenhum dado de tarefa foi alterado."
          : (error?.message || "Não foi possível alterar o status do funcionário."));
      }
    }

    function handleEmployeeManagementAction(event) {
      const button = event.target.closest("button[data-employee-action]");
      if (!button) return;
      const employee = employees.find(item => item.id === button.dataset.id);
      if (!employee) return;
      if (button.dataset.employeeAction === "edit") {
        openEmployeeManagementModal(employee);
        return;
      }
      if (button.dataset.employeeAction === "toggle") toggleEmployeeActive(employee);
    }

'''
replace_once(employee_helpers_anchor, employee_helpers + employee_helpers_anchor, 'employee helpers')

# Employee lookups and task history must not discard names merely because someone is inactive.
replace_once(
    '''    function getEmployeeColor(employeeName) {
      if (employeeName === "todos") return "var(--red)";
      return employees.find(employee => employee.name === employeeName)?.color || "var(--red)";
    }''',
    '''    function getEmployeeColor(employeeName) {
      if (employeeName === "todos") return "var(--red)";
      return getEmployeeByName(employeeName)?.color || "#64748b";
    }''',
    'employee color helper',
)
replace_once(
    '''      return [...new Set(names
        .map(name => String(name || "").trim())
        .filter(name => employees.some(employee => employee.name === name)))];''',
    '''      return [...new Set(names
        .map(name => String(name || "").trim())
        .filter(Boolean))];''',
    'preserve historical assignees',
)

# Selector shows inactive historical people for reporting/visibility, but identifies them clearly.
replace_once(
    '''      const options = [{ name: "todos", label: "Todos", color: "var(--red)" }, ...employees.map(employee => ({
        name: employee.name,
        label: employee.name,
        color: employee.color
      }))];''',
    '''      const options = [{ name: "todos", label: "Todos", color: "var(--red)" }, ...employees.map(employee => ({
        name: employee.name,
        label: `${employee.name}${employee.active === false ? " · inativo" : ""}`,
        color: employee.color
      }))];''',
    'selector inactive label',
)

# Build task assignee choices from roster. Inactive employees remain visible but disabled,
# so editing an old task does not silently lose its historical assignee.
build_employees_old = '''    function buildEmployees() {
      employeeInput.innerHTML = "";
      const reportEmployeeInput = document.getElementById("reportEmployeeInput");
      if (reportEmployeeInput) reportEmployeeInput.innerHTML = "";

      const admin = isAdminUser() || !currentUserProfile;
      const ownEmployee = currentEmployeeName();

      employees.forEach(employee => {
        const label = document.createElement("label");
        label.className = "employee-check";
        label.innerHTML = `
          <input type="checkbox" name="taskEmployees" value="${escapeHTML(employee.name)}">
          <span class="employee-check-name">
            <span class="dot" style="color:${escapeHTML(employee.color)}"></span>
            <span>${escapeHTML(employee.name)}</span>
          </span>
        `;
        const checkbox = label.querySelector("input");
        checkbox.disabled = false;
        employeeInput.appendChild(label);
      });

      if (reportEmployeeInput) {
        if (admin) {
          const reportAll = document.createElement("option");
          reportAll.value = "todos";
          reportAll.textContent = "Todos";
          reportEmployeeInput.appendChild(reportAll);
        }

        employees.forEach(employee => {
          const reportOption = document.createElement("option");
          reportOption.value = employee.name;
          reportOption.textContent = employee.name;
          reportEmployeeInput.appendChild(reportOption);
        });

        reportEmployeeInput.disabled = !admin;
        reportEmployeeInput.value = admin ? (reportEmployeeInput.value || "todos") : ownEmployee;
      }

      selectedEmployee = admin ? (selectedEmployee || "todos") : ownEmployee;
      if (!selectedEmployee || (!admin && selectedEmployee !== ownEmployee)) selectedEmployee = admin ? "todos" : ownEmployee;

      updateEmployeeSelector();
    }'''
build_employees_new = '''    function buildEmployees() {
      employeeInput.innerHTML = "";
      const reportEmployeeInput = document.getElementById("reportEmployeeInput");
      const previousReportEmployee = reportEmployeeInput?.value || "todos";
      if (reportEmployeeInput) reportEmployeeInput.innerHTML = "";

      const admin = isAdminUser() || !currentUserProfile;
      const ownEmployee = currentEmployeeName();

      employees.forEach(employee => {
        const inactive = employee.active === false;
        const label = document.createElement("label");
        label.className = "employee-check";
        label.innerHTML = `
          <input type="checkbox" name="taskEmployees" value="${escapeHTML(employee.name)}" ${inactive ? "disabled" : ""}>
          <span class="employee-check-name">
            <span class="dot" style="color:${escapeHTML(employee.color)}"></span>
            <span>${escapeHTML(employee.name)}${inactive ? " · inativo" : ""}</span>
          </span>
        `;
        employeeInput.appendChild(label);
      });

      if (reportEmployeeInput) {
        if (admin) {
          const reportAll = document.createElement("option");
          reportAll.value = "todos";
          reportAll.textContent = "Todos";
          reportEmployeeInput.appendChild(reportAll);
        }

        employees.forEach(employee => {
          const reportOption = document.createElement("option");
          reportOption.value = employee.name;
          reportOption.textContent = `${employee.name}${employee.active === false ? " (inativo)" : ""}`;
          reportEmployeeInput.appendChild(reportOption);
        });

        reportEmployeeInput.disabled = !admin;
        const allowedValue = Array.from(reportEmployeeInput.options).some(option => option.value === previousReportEmployee)
          ? previousReportEmployee
          : (admin ? "todos" : ownEmployee);
        reportEmployeeInput.value = admin ? allowedValue : ownEmployee;
      }

      selectedEmployee = admin ? (selectedEmployee || "todos") : ownEmployee;
      if (!selectedEmployee || (!admin && selectedEmployee !== ownEmployee)) selectedEmployee = admin ? "todos" : ownEmployee;

      updateEmployeeSelector();
    }'''
replace_once(build_employees_old, build_employees_new, 'build employees')

# Header and card color use compatibility lookup.
replace_once(
    '''      const employee = employees.find(item => item.name === selectedEmployee);
      pageTitle.textContent = `Serviços de ${selectedEmployee}`;
      pageSubtitle.textContent = `Painel individual com cor própria para ${selectedEmployee}.`;
      document.documentElement.style.setProperty("--red", employee?.color || "#e50914");''',
    '''      const employee = getEmployeeByName(selectedEmployee);
      pageTitle.textContent = `Serviços de ${selectedEmployee}`;
      pageSubtitle.textContent = employee?.active === false
        ? `Histórico de ${selectedEmployee}. Funcionário inativo para novas atribuições.`
        : `Painel individual com cor própria para ${selectedEmployee}.`;
      document.documentElement.style.setProperty("--red", employee?.color || "#e50914");''',
    'inactive header',
)
replace_once(
    '      card.style.borderTop = `3px solid ${employees.find(e => e.name === mainEmployee)?.color || "var(--red)"}`;',
    '      card.style.borderTop = `3px solid ${getEmployeeColor(mainEmployee)}`;',
    'task card employee color',
)
replace_once(
    '      const defaultEmployee = currentUserProfile?.employee || employees[0].name;',
    '      const defaultEmployee = currentUserProfile?.employee || getActiveEmployees()[0]?.name || employees[0]?.name || "";',
    'new task active default',
)

# Firestore employee listener, designed to fail soft: tasks/clients keep operating if
# the new collection is not yet allowed by current Firebase rules.
listen_clients_anchor = '''    function listenClients() {'''
listen_employees = r'''    function listenEmployees() {
      if (unsubscribeEmployees) unsubscribeEmployees();
      unsubscribeEmployees = onSnapshot(collection(db, "funcionarios"), (snapshot) => {
        const firebaseEmployees = snapshot.docs.map(docSnap => ({ id: docSnap.id, ...docSnap.data(), source: "firebase" }));
        employees = mergeEmployeeRoster(firebaseEmployees);
        enrichEmployeesFromTasks();
        buildEmployees();
        renderEmployeesManagement();
        render();
      }, (error) => {
        console.error(error);
        employees = mergeEmployeeRoster([]);
        enrichEmployeesFromTasks();
        buildEmployees();
        renderEmployeesManagement();
        render();
        if (isAdminUser()) {
          showToast("Equipe carregada no modo compatível. A coleção funcionarios ainda não está liberada nas regras do Firestore.");
        }
      });
    }

'''
replace_once(listen_clients_anchor, listen_employees + listen_clients_anchor, 'employee listener')

# Task subscription enriches unknown historical names rather than hiding them.
replace_once(
    '''          });
        render();
      }, (error) => {''',
    '''          });
        const rosterChanged = enrichEmployeesFromTasks();
        if (rosterChanged && !taskModal.classList.contains("open")) buildEmployees();
        renderEmployeesManagement();
        render();
      }, (error) => {''',
    'task listener historical enrich',
)

# Login/logout subscription lifecycle and admin-only Team module visibility.
replace_once(
    '      document.getElementById("importBackupBtn").style.display = isAdminUser() ? "inline-flex" : "none";\n      loginScreen.style.display = "none";',
    '      document.getElementById("importBackupBtn").style.display = isAdminUser() ? "inline-flex" : "none";\n      document.getElementById("viewEmployeesBtn").style.display = isAdminUser() ? "flex" : "none";\n      loginScreen.style.display = "none";',
    'team nav admin visibility',
)
replace_once(
    '      listenTasks();\n      listenClients();\n      remindAdminBackup();',
    '      listenEmployees();\n      listenTasks();\n      listenClients();\n      remindAdminBackup();',
    'employee listener start',
)
replace_once(
    '      if (unsubscribeClients) unsubscribeClients();\n      tasks = [];\n      clients = [];',
    '      if (unsubscribeClients) unsubscribeClients();\n      if (unsubscribeEmployees) unsubscribeEmployees();\n      tasks = [];\n      clients = [];\n      employees = defaultEmployees.map(employee => ({ ...employee }));',
    'employee listener logout',
)
replace_once(
    '      document.getElementById("importBackupBtn").style.display = "none";\n      render();',
    '      document.getElementById("importBackupBtn").style.display = "none";\n      document.getElementById("viewEmployeesBtn").style.display = "none";\n      renderEmployeesManagement();\n      render();',
    'team nav logout',
)

# Event wiring for Team module + modal.
replace_once(
    '    document.getElementById("viewReportsBtn").addEventListener("click", () => setView("reports"));\n',
    '    document.getElementById("viewReportsBtn").addEventListener("click", () => setView("reports"));\n    document.getElementById("viewEmployeesBtn").addEventListener("click", () => setView("employees"));\n    document.getElementById("openEmployeeModalBtn").addEventListener("click", () => openEmployeeManagementModal());\n    document.getElementById("employeesTableBody").addEventListener("click", handleEmployeeManagementAction);\n    document.getElementById("employeeManagementForm").addEventListener("submit", saveEmployeeManagement);\n    document.getElementById("closeEmployeeManagementModalBtn").addEventListener("click", closeEmployeeManagementModal);\n    document.getElementById("cancelEmployeeManagementBtn").addEventListener("click", closeEmployeeManagementModal);\n    document.getElementById("employeeManagementModal").addEventListener("click", event => {\n      if (event.target === document.getElementById("employeeManagementModal")) closeEmployeeManagementModal();\n    });\n',
    'team events',
)

# Initial/teardown lifecycle.
replace_once(
    '    buildEmployees();\n    render();\n    startFirebase();',
    '    buildEmployees();\n    renderEmployeesManagement();\n    render();\n    startFirebase();',
    'initial team render',
)
replace_once(
    '      if (unsubscribeClients) unsubscribeClients();\n    });',
    '      if (unsubscribeClients) unsubscribeClients();\n      if (unsubscribeEmployees) unsubscribeEmployees();\n    });',
    'employee unsubscribe before unload',
)

path.write_text(text, encoding="utf-8")
print("Employee management patch applied successfully.")
