import pandas as pd


df_sibling1 = pd.DataFrame({
    "Name" : ["SHLOK", "SHREYA", "SHUBHAM"],
    "Age" : [22,32,30],
})

df_sibling2 = pd.DataFrame({
    "Name" : ["Choti", "MT", "Chota"],
    "Age": [18,16,11]
})


df_concat = pd.concat([df_sibling1, df_sibling2], ignore_index=True)

df_concat = pd.concat([df_sibling1, df_sibling2], axis=1, ignore_index=True)


print(df_concat)