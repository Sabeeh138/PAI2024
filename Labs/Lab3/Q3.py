
number = int(input("Enter the number of elements for both lists: "))

list1 = []
list2 = []

print("Enter strings for the first list:")
for i in range(number):
    string = input(f"String {i + 1}: ")
    list1.append(string)
print("Enter numbers for the second list:")
for i in range(number):
    numbers = int(input(f"Number {i + 1}: "))
    list2.append(numbers)

dictionary = dict(zip(list1, list2))

# Write the dictionary to a text file
with open('dictionary.txt', 'w') as file:
    file.write(str(dictionary))

print("Dictionary saved to dictionary.txt.")
