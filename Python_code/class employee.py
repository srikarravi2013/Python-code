class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = float(salary)

    def give_raise(self, percent):
        if percent > 0:
            self.salary += self.salary * (percent / 100.0)
            return self.salary
        raise ValueError("Raise percentage must be positive.")

    def display(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:,.2f}")


emp = Employee(employee_id="E101", name="Jane Doe", salary=75000.0)

print("Employee Details:")
emp.display()

# Give a 10% raise
emp.give_raise(10.0)
print("\nEmployee Details After 10% Raise:")
emp.display()