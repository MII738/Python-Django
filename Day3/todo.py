import sys
import json
from pathlib import Path

TODO_FILE = Path(__file__).parent / "data" / "todo.json"


def load_tasks():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("✅ No tasks for now!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. [{status}] {task['task']}")


def add_task(task_desc):
    tasks = load_tasks()
    tasks.append({"task": task_desc, "done": False})
    save_tasks(tasks)
    print(f"➕ Added task: {task_desc}")


def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✅ Marked task {index} as done.")
    else:
        print("⚠️ Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['task']}")
    else:
        print("⚠️ Invalid task number.")


if __name__ == "__main__":
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
            print("Please enter correct command")
    else:
        print("Please enter correct command")
