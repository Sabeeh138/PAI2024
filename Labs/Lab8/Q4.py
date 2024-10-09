import numpy as np
dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'U10')]
data = np.array([
    ('Alice', 5.5, '10th'),
    ('Bob', 5.7, '9th'),
    ('Charlie', 5.5, '10th'),
    ('David', 6.0, '9th'),
    ('Eve', 5.3, '10th'),
], dtype=dtype)
sorted_data = np.sort(data, order=['class', 'height'])
print("Sorted Structured Array:")
print(sorted_data)
