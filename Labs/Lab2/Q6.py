def multilist(numbers):
    result = 1
    
    for number in numbers:
        result *= number
    return result
    
numbers = [2, 3, 4, 5]
print(f"The product of the numbers in the nymber list is: {multilist(numbers)}")
