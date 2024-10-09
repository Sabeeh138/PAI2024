import numpy as np

choices = [2, 5, 9, 10]
random_matrix = np.random.choice(choices, size=(4, 4))

identity_matrix = np.eye(4)

multiplied_matrix = random_matrix @ identity_matrix

odd_matrix = np.arange(1, 33, 2).reshape(4, 4)

resultant_matrix = multiplied_matrix + odd_matrix

print("Random Matrix:")
print(random_matrix)
print("\nIdentity Matrix:")
print(identity_matrix)
print("\nMultiplied Matrix (same as Random Matrix):")
print(multiplied_matrix)
print("\nOdd Matrix:")
print(odd_matrix)
print("\nResultant Matrix after Addition:")
print(resultant_matrix)
