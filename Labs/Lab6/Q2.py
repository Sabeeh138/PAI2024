import pandas as pd

# Sample data: Create a DataFrame with movie data including runtime
data = {
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Revenue': [2.5e6, 1.5e6, 3.0e6, 0.8e6, 2.1e6],
    'Budget': [0.9e6, 0.5e6, 0.7e6, 1.2e6, 0.4e6],
    'Runtime': [120, 95, 150, 85, 110]  # Runtime in minutes
}

movies_df = pd.DataFrame(data)
sorted_movies = movies_df.sort_values(by='Runtime', ascending=False)
print(sorted_movies)
