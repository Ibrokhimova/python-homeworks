class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    @staticmethod
    def from_string(data):
        parts = data.strip().split(', ')
        return Employee(parts[0], parts[1], parts[2], parts[3])


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self):
        eid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        emp = Employee(eid, name, position, salary)
        with open(self.filename, 'a') as file:
            file.write(str(emp) + '\n')
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("No employee records found.")
                else:
                    print("Employee Records:")
                    for line in lines:
                        print(line.strip())
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self):
        eid = input("Enter Employee ID to search: ")
        found = False
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    emp = Employee.from_string(line)
                    if emp.employee_id == eid:
                        print("Employee Found:")
                        print(emp)
                        found = True
                        break
            if not found:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def update_employee(self):
        eid = input("Enter Employee ID to update: ")
        updated = False
        employees = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    emp = Employee.from_string(line)
                    if emp.employee_id == eid:
                        print("Enter new details:")
                        emp.name = input("New Name: ")
                        emp.position = input("New Position: ")
                        emp.salary = input("New Salary: ")
                        updated = True
                    employees.append(emp)

            if updated:
                with open(self.filename, 'w') as file:
                    for emp in employees:
                        file.write(str(emp) + '\n')
                print("Employee updated successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self):
        eid = input("Enter Employee ID to delete: ")
        deleted = False
        employees = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    emp = Employee.from_string(line)
                    if emp.employee_id != eid:
                        employees.append(emp)
                    else:
                        deleted = True

            if deleted:
                with open(self.filename, 'w') as file:
                    for emp in employees:
                        file.write(str(emp) + '\n')
                print("Employee deleted successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def run(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()
