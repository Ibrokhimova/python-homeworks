import json
import csv
import os

tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

TASKS_JSON = "tasks.json"

def create_tasks_file():
    if not os.path.exists(TASKS_JSON):
        with open(TASKS_JSON, "w") as file:
            json.dump(tasks_data, file, indent=4)
        print(f"'{TASKS_JSON}' fayli yaratildi.")
    else:
        print(f"'{TASKS_JSON}' fayli allaqachon mavjud.")

def load_tasks():
    with open(TASKS_JSON, "r") as file:
        tasks = json.load(file)
    return tasks
def display_tasks(tasks):
    print("\n--- Vazifalar ro'yxati ---")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")
    print("--------------------------\n")

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed
    avg_priority = sum(task["priority"] for task in tasks) / total if total > 0 else 0
    print("--- Vazifalar Statistikasi ---")
    print(f"Jami vazifalar: {total}")
    print(f"Yakunlangan vazifalar: {completed}")
    print(f"Kutilayotgan vazifalar: {pending}")
    print(f"O'rtacha ustuvorlik: {avg_priority:.2f}")
    print("------------------------------\n")
def save_tasks_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["ID", "Task", "Completed", "Priority"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "ID": task["id"],
                "Task": task["task"],
                "Completed": task["completed"],
                "Priority": task["priority"]
            })
    print(f"Vazifalar '{filename}' fayliga saqlandi.")
def update_task(tasks, task_id, completed=None, priority=None, task_name=None):
    for task in tasks:
        if task["id"] == task_id:
            if completed is not None:
                task["completed"] = completed
            if priority is not None:
                task["priority"] = priority
            if task_name is not None:
                task["task"] = task_name
            print(f"Vazifa ID={task_id} yangilandi.")
            return True
    print(f"Vazifa ID={task_id} topilmadi.")
    return False

def save_tasks_to_json(tasks):
    with open(TASKS_JSON, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Vazifalar '{TASKS_JSON}' fayliga yangilandi.")

if __name__ == "__main__":

    create_tasks_file()
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    save_tasks_to_csv(tasks)
    update_task(tasks, task_id=3, completed=True)
    save_tasks_to_json(tasks)
    display_tasks(tasks)
    calculate_stats(tasks)
