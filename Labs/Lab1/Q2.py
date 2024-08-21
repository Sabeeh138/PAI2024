num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operand = input("enter the operand (+, -, * , / : ")

if operand == '-':
    result = print(num1 - num2)
    
elif operand == '*':
    result = print(num1 * num2)
    
elif operand == '/':
    result = print(num1 / num2)

elif operand == '+':
    result = print(num1 - (-num2))

else :
    print("Invalid operand, please try again")
    
print(f"The result is: {result}")
