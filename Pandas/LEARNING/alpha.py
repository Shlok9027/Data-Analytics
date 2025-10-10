import pandas as pd

data = pd.Series(
     ["Shlok", "Shreya", "Shubham", "Shlok"],
)




print(data.str.upper())
print(data.str.lower())
print(data.str.len())
print(data.str.startswith("Sh"))
print(data.str.isupper()
)