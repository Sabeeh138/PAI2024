class Employee:
    def __init__(self):
        self.name = ""
        self.monthly_salary = 0.0
        self.tax_percentage = 2.0  # Default tax percentage is 2%
    
    def get_data(self):
        self.name = input("Enter employee name: ")
        self.monthly_salary = float(input("Enter monthly salary: "))
        self.tax_percentage = float(input("Enter percentage of tax: "))

    def salary_after_tax(self):
        tax_amount = (self.tax_percentage / 100) * self.monthly_salary
        remaining_salary = self.monthly_salary - tax_amount
        return remaining_salary

    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage

employee = Employee()
employee.get_data()

print(f"Salary after tax: ${employee.salary_after_tax():.2f}")


new_tax_percentage = float(input("Enter new tax percentage: "))
employee.update_tax_percentage(new_tax_percentage)

print(f"Salary after tax with updated percentage: ${employee.salary_after_tax():.2f}")
