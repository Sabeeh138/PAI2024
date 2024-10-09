import pandas as pd
file_path = 'employee.xlsx'  
df = pd.read_excel(file_path)
print("DataFrame is now Loaded:")
print(df.head())  
specified_year = 2023  
employees_of_year = df[df['Year'] == specified_year]  
print(f"\nEmployees of the year {specified_year}:")
print(employees_of_year)
