import json
import csv
import os

class Task:
    def __init__(self, task_id, title, description, due_date='', status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)

class StorageStrategy:
    def save(self, tasks, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError

class JSONStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]

class CSVStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=tasks[0].to_dict().keys())
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            return [Task.from_dict(row) for row in reader]

class ToDoApp:
    def __init__(self, storage_strategy: StorageStrategy, filename='tasks.json'):
        self.storage = storage_strategy
        self.filename = filename
        self.tasks = self.storage.load(self.filename)

    def add_task(self):
        task_id = input("Enter Task ID: ")
        if any(task.task_id == task_id for task in self.tasks):
            print("Task ID must be unique!")
            return
        title = input("Enter Title: ")
        desc = input("Enter Description: ")
        due = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, desc, due, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        sort_key = input("Sort by (task_id/title/due_date/status)? Press Enter to skip: ")
        if sort_key:
            self.tasks.sort(key=lambda x: getattr(x, sort_key, ''))
        for t in self.tasks:
            print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input(f"New Title (current: {task.title}): ") or task.title
                task.description = input(f"New Description (current: {task.description}): ") or task.description
                task.due_date = input(f"New Due Date (current: {task.due_date}): ") or task.due_date
                task.status = input(f"New Status (current: {task.status}): ") or task.status
                print("Task updated.")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) < initial_len:
            print("Task deleted.")
        else:
            print("Task not found.")

    def filter_tasks(self):
        status = input("Enter status to filter (Pending/In Progress/Completed): ")
        filtered = [t for t in self.tasks if t.status == status]
        for t in filtered:
            print(f"{t.task_id}, {t.title}, {t.description}, {t.due_date}, {t.status}")

    def save_tasks(self):
        self.storage.save(self.tasks, self.filename)
        print("Tasks saved.")

    def load_tasks(self):
        self.tasks = self.storage.load(self.filename)
        print("Tasks loaded.")

    def run(self):
        while True:
            print("\nTo-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")

            try:
                if choice == '1': self.add_task()
                elif choice == '2': self.view_tasks()
                elif choice == '3': self.update_task()
                elif choice == '4': self.delete_task()
                elif choice == '5': self.filter_tasks()
                elif choice == '6': self.save_tasks()
                elif choice == '7': self.load_tasks()
                elif choice == '8': break
                else: print("Invalid choice.")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == '__main__':
    print("Choose storage format: 1. JSON  2. CSV")
    fmt = input("Enter choice: ")
    if fmt == '2':
        app = ToDoApp(CSVStorage(), 'tasks.csv')
    else:
        app = ToDoApp(JSONStorage(), 'tasks.json')
    app.run()
