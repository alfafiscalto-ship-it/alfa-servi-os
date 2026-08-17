from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

old = '''      const employeeId = editingEmployeeId || employeeSlug(name) || doc(collection(db, "funcionarios")).id;
      const submitButton = document.querySelector('#employeeManagementForm button[type="submit"]');'''
new = '''      const employeeId = editingEmployeeId || employeeSlug(name) || doc(collection(db, "funcionarios")).id;
      const wasEditing = Boolean(editingEmployeeId);
      const submitButton = document.querySelector('#employeeManagementForm button[type="submit"]');'''

if text.count(old) != 1:
    raise SystemExit(f"employeeId anchor expected once, found {text.count(old)}")
text = text.replace(old, new, 1)

old_toast = '''        closeEmployeeManagementModal();
        showToast(editingEmployeeId ? "Funcionário atualizado." : "Funcionário adicionado à equipe.");'''
new_toast = '''        closeEmployeeManagementModal();
        showToast(wasEditing ? "Funcionário atualizado." : "Funcionário adicionado à equipe.");'''

if text.count(old_toast) != 1:
    raise SystemExit(f"toast anchor expected once, found {text.count(old_toast)}")
text = text.replace(old_toast, new_toast, 1)

path.write_text(text, encoding="utf-8")
print("Employee management toast fix applied.")
