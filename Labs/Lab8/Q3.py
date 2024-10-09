import numpy as np
even_numbers = np.arange(2, 20, 2).reshape(3, 3)
multiplied_matrix = even_numbers * 4
identity_matrix = np.eye(3)
resultant_matrix = multiplied_matrix @ identity_matrix
print("Original 3x3 Even Numbers")
print(even_numbers)
print("\nMultiplied Matrix by 4")
print(multiplied_matrix)
print("\nResultant Matrix")
print(resultant_matrix)
