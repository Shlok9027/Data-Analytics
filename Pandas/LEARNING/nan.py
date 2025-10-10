import numpy as np
import pandas as pd

data = {
    'FirstName': ['Vipul', 'Ashish', 'Milan'],
    "Gender": ["", "", ""],
    "Age": [0, 0, 0]
}

df = pd.DataFrame(data)
print(df)

df['Department'] = np.nan

print(df)


df.dropna(how='all',axis=1, inplace=True)

print(df)