numbers = list(map(int,input("Enter a list of numbers :").split()))

target = int(input("Enter the target number: "))
numbers = [num for num in numbers if num>=target]

print(f"The updated list with the elements >={target} is : {numbers}")
