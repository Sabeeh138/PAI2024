import pandas as pd

dictionary = {
    "Name": ["sabeeh","abbas","huzaifa"],
    "Score": [3.99, 3.50, 3.89]
}
reindex=['a','b','c']
df=pd.DataFrame(dictionary, index= reindex)
print(df)
