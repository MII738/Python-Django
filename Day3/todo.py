import sys
import json
from pathlib import Path

TODO_FILE = Path(__file__).parent / "data" / "todo.json"


def load_tasks():
    try:
        if TODO_FILE.exists():
            with open(TODO_FILE, "r") as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️ Error reading tasks: {e}")
    return []


def save_tasks(tasks):
    try:
        TODO_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(TODO_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"⚠️ Error saving tasks: {e}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("✅ No tasks for now!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task.get("done") else "❌"
            print(f"{i}. [{status}] {task.get('task', 'Unknown task')}")


def add_task(task_desc):
    if not isinstance(task_desc, str):
        print("❗ Task description must be a string.")
        return

    task_desc = task_desc.strip()
    if not task_desc:
        print("❗ Task description cannot be empty.")
        return

    if task_desc.isnumeric():
        print("❗ Task description cannot be only numbers.")
        return

    tasks = load_tasks()
    tasks.append({"task": task_desc, "done": False})
    save_tasks(tasks)
    print(f"➕ Added task: {task_desc}")


def mark_done(index):
    try:
        tasks = load_tasks()
        if 0 < index <= len(tasks):
            tasks[index - 1]["done"] = True
            save_tasks(tasks)
            print(f"✅ Marked task {index} as done.")
        else:
            print("⚠️ Invalid task number.")
    except (ValueError, TypeError) as e:
        print(f"⚠️ Error marking task as done: {e}")

def show_help():
    print("""
        📝 To-Do CLI
        Usage:
        python todo.py list              Show all tasks
        python todo.py add "task name"  Add a new task
        python todo.py done <task_no>   Mark a task as done
        python todo.py del <task_no>    Delete a task
        """)
def delete_task(index):
    try:
        tasks = load_tasks()
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("⚠️ Invalid task number.")
    except (ValueError, TypeError) as e:
        print(f"⚠️ Error deleting task: {e}")

        


if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            command = sys.argv[1]
            if command == "list":
                list_tasks()
            elif command == "add" and len(sys.argv) > 2:
                add_task(" ".join(sys.argv[2:]))
            elif command == "done" and len(sys.argv) == 3:
                mark_done(int(sys.argv[2]))
            elif command == "del" and len(sys.argv) == 3:
                delete_task(int(sys.argv[2]))
            else:
                print("❗ Please enter a correct command.")
        else:
            print("❗ Please enter a command.")
            show_help()
    except Exception as e:
        print(f"🔥 An unexpected error occurred: {e}")
