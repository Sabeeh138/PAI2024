import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = pd.read_csv('heart.csv')

X = data.drop(columns=['target'])  # Features
y = data['target']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

k_values = range(1, 251)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

highest_accuracy = max(accuracies)
lowest_accuracy = min(accuracies)
best_k = k_values[np.argmax(accuracies)]
worst_k = k_values[np.argmin(accuracies)]

print(f"Highest accuracy: {highest_accuracy:.4f} at k={best_k}")
print(f"Lowest accuracy: {lowest_accuracy:.4f} at k={worst_k}")

plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, marker='o')
plt.title('Accuracy vs. Number of Neighbors (k)')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.grid()
plt.show()
