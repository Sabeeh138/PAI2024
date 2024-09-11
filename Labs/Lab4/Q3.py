class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printdata(self):
            print(f"Name: {self.name}, Age: {self.age}")
            
student1 = Student("Hamza Abbas Sabeeh", 21)
student1.printdata()
