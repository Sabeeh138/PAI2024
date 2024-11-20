import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('heart.csv')


X = data.drop(columns=['target'])  # Features
y = data['target']  # Target


random_seeds = range(1, 11)
seed_accuracies = []


for seed in random_seeds:
    # Split data with the current random seed
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    seed_accuracies.append((seed, acc))


highest_seed, highest_accuracy = max(seed_accuracies, key=lambda x: x[1])
lowest_seed, lowest_accuracy = min(seed_accuracies, key=lambda x: x[1])


print("Accuracies for different random seeds:")
for seed, acc in seed_accuracies:
    print(f"Random seed {seed}: Accuracy = {acc:.4f}")


print(f"\nHighest accuracy: {highest_accuracy:.4f} (Random seed = {highest_seed})")
print(f"Lowest accuracy: {lowest_accuracy:.4f} (Random seed = {lowest_seed})")
