def employee(name, salary=10000):
    taxrate = 0.02
    salaryaftertax = salary * (1 - taxrate)
    print(f"Name of the Employtee is : {name}")
    print(f"Salary of the employee after taxation is: ${salaryaftertax}")

employee("Sabeeh", 50000)
employee("Haris huzaiifa abbas")
