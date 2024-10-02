import pandas as pd
df = pd.read_csv('path_to_your_dataset.csv')
print(df.head())
print(df.columns)
filtered_df = df[df['Year'].isin([1987, 1989])]
print(filtered_df)
