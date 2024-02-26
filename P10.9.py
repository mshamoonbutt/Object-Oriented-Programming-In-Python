class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return f"Manager: {self.name}, Department: {self._department}, Salary: {self.salary}"

class Executive(Manager):
    def __repr__(self):
        return f"Executive: {self.name}, Department: {self._department}, Salary: {self.salary}"

# Test program
employee = Employee("John Doe", 50000)
manager = Manager("Jane Smith", 70000, "Sales")
executive = Executive("Mike Johnson", 100000, "Finance")

print(employee)
print(manager)
print(executive)