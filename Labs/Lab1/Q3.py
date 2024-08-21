evencount = 0
numbers = input("enter a list of integers seperated by spaces: ")

for num in numbers.split():
    if int(num) % 2 == 0:
        evencount += 1
        
print(f"the even count of the number list is {evencount}")
