import pandas as pd

# data = {
#     "Name" : ["Shlok", "Shreya", "Shubham"],
#     "Age" : [22,32,30],
#     "Salary": [45000,52000,70000]
# }

# df = pd.DataFrame(data)

# print(df)

# df.sort_values(by="Age", ascending=True, inplace=True)

# print(df)


import pandas as pd

data = {
    "Name" : ["Shlok", "Shreya", "Shubham"],
    "Age" : [22,32,30],
    "Salary": [45000,52000,70000]
}

df = pd.DataFrame(data)

print(df)

df.sort_values(by=["Age", "Salary"], ascending=[True,True], inplace=True)

print(df)


avg_salary = df["Salary"].mean()
print(avg_salary)