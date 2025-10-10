import pandas as pd

# df = pd.read_json("output.json")

df = pd.read_json("dummy_json_data.json")

print("Printing First 10 Rows")
print(df.head(10))

# print(df)

print("Printing First 10 Column")
print(df.tail(10))
