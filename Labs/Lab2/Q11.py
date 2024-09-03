
students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [95, 100, 93]
}


def add_grade(student_name, grade):
    if student_name in students:
        students[student_name].append(grade)
        print(f"Added grade {grade} to {student_name}'s grades.")
    else:
        print(f"Student {student_name} does not exist.")


def calculate_average(student_name):
    if student_name in students and students[student_name]:
        average = sum(students[student_name]) / len(students[student_name])
        print(f"{student_name}'s average grade is {average:.2f}.")
    else:
        print(f"Student {student_name} does not exist or has no grades.")


def add_student(student_name):
    if student_name not in students:
        students[student_name] = []
        print(f"Student {student_name} has been added.")
    else:
        print(f"Student {student_name} already exists.")


def remove_student(student_name):
    if student_name in students:
        del students[student_name]
        print(f"Student {student_name} has been removed.")
    else:
        print(f"Student {student_name} does not exist.")


        print("\nChoose an operation:")
        print("1. Add a new grade to a student's list of grades")
        print("2. Calculate and print the average grade for a specific student")
        print("3. Add a new student with an initial empty list of grades")
        print("4. Remove a student from the dictionary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            student_name = input("Enter the student's name: ")
            try:
                grade = float(input("Enter the grade to add: "))
                add_grade(student_name, grade)
            except ValueError:
                print("Invalid input! Please enter a numeric grade.")

        elif choice == '2':
            student_name = input("Enter the student's name: ")
            calculate_average(student_name)

        elif choice == '3':
            student_name = input("Enter the new student's name: ")
            add_student(student_name)

        elif choice == '4':
            student_name = input("Enter the student's name to remove: ")
            remove_student(student_name)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


