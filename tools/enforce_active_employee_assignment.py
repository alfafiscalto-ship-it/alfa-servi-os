from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

old_modal = '''      } else if (admin && selectedEmployee && selectedEmployee !== "todos") {
        selectedNames = [selectedEmployee];
      } else {'''
new_modal = '''      } else if (admin && selectedEmployee && selectedEmployee !== "todos" && getEmployeeByName(selectedEmployee)?.active !== false) {
        selectedNames = [selectedEmployee];
      } else {'''
if text.count(old_modal) != 1:
    raise SystemExit(f"openModal active guard anchor expected once, found {text.count(old_modal)}")
text = text.replace(old_modal, new_modal, 1)

old_save = '''      const selectedClient = parseClientInput(document.getElementById("clientInput").value);
      let selectedEmployees = getSelectedTaskEmployees();


      const payload = {'''
new_save = '''      const selectedClient = parseClientInput(document.getElementById("clientInput").value);
      let selectedEmployees = getSelectedTaskEmployees();

      // Funcionários inativos continuam em tarefas históricas já existentes,
      // mas nunca podem ser adicionados a uma tarefa nova.
      if (!editingTaskId) {
        selectedEmployees = selectedEmployees.filter(name => getEmployeeByName(name)?.active !== false);
      }

      const payload = {'''
if text.count(old_save) != 1:
    raise SystemExit(f"saveTask active guard anchor expected once, found {text.count(old_save)}")
text = text.replace(old_save, new_save, 1)

path.write_text(text, encoding="utf-8")
print("Active employee assignment guard applied.")
