class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

    def hire(self):
        print(f"{self.name} is hiring someone.")


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

    def write_code(self):
        print(f"{self.name} is writing code.")


class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30



manager = Manager("haris", 80000)
developer = Developer("Basit", 60000)
senior_manager = SeniorManager("arthur morgan", 100000)

print(f"{manager.name}'s bonus: ${manager.calculate_bonus():.2f}")
print(f"{developer.name}'s bonus: ${developer.calculate_bonus():.2f}")
print(f"{senior_manager.name}'s bonus: ${senior_manager.calculate_bonus():.2f}")

manager.hire()
developer.write_code()
