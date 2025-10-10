import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df = pd.DataFrame(data)

print(df)

df_no_duplicates = df.drop_duplicates()

print(df_no_duplicates)