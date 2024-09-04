try:
    name=input("enter your name")
    cnic=input("enter the cnic")
    age=input("enter the age")
    salary=input("enter the slary")
    content=name + cnic +age +salary
    with open("od.txt","w") as file:
        file.write(content)
    appending=input("enter ur contact number")
    with open("od.text", "a") as file:
        file.append(appending)
except FileNotFoundError:
    print("Error, File could not be found")
except IOError:
    print("Error, IO not found")
except Exception as e:
    print(f"An unexpected error occured{e}")
