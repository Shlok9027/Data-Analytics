import pandas as pd


df = pd.read_csv("Annunal.csv")
print(df.head())

bool_series = pd.isnull(df['Industry_aggregation_NZSIOC'])

missing_data = df[bool_series]

print(missing_data)