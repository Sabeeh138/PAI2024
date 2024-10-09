import numpy as np
odd_numbers = np.arange(1, 19, 2)
odd_array = odd_numbers.reshape(3, 3)
print("3x3 Array of odd numbers:")
print(odd_array)
print("\nIterating over the array:")
for row in odd_array:
    for element in row:
        print(element)
