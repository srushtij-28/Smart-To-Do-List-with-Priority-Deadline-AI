from datetime import datetime

tasks = []

def add_task():
    name = input("Task name: ")
    due = input("Due date (YYYY-MM-DD): ")
    priority = int(input("Priority (1-5): "))

    due_date = datetime.strptime(due, "%Y-%m-%d")
    days_left = (due_date - datetime.now()).days

    urgency = max(1, 10 - days_left) * priority

    tasks.append({
        "name": name,
        "due": due_date,
        "priority": priority,
        "urgency": urgency
    })

    print("✅ Task added.")

def show_tasks():
    sorted_tasks = sorted(tasks, key=lambda x: x["urgency"], reverse=True)
    print("\n📋 Smart Task List")
    for t in sorted_tasks:
        print(f"{t['name']} | Due: {t['due'].date()} | Urgency: {t['urgency']}")

while True:
    print("\nDay 81 — Smart To-Do")
    print("1. Add Task")
    print("2. Show Smart List")
    print("3. Exit")

    c = input("Choose: ")
    if c == "1":
        add_task()
    elif c == "2":
        show_tasks()
    elif c == "3":
        break
