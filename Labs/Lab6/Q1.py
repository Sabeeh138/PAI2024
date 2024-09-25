import pandas as pd


data = {
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Revenue': [2.5e6, 1.5e6, 3.0e6, 0.8e6, 2.1e6],  
    'Budget': [0.9e6, 0.5e6, 0.7e6, 1.2e6, 0.4e6]   
}

movies_df = pd.DataFrame(data)
filtered_movies = movies_df[(movies_df['Revenue'] > 2e6) & (movies_df['Budget'] < 1e6)]


print(filtered_movies)
