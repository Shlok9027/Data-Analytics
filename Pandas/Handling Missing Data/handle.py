import pandas as pd 

data  = {
    "Name" : ["Shlok" ,"None", "Shreya", "Shubham" , "Ankit" , "Ankita"],

    "Age" : [22,None, 26, 30, 37, 24],

    "Salary" : [45000,None, 52000, 70000, 49000, 55000],

    "Performance_Score" : [97 ,None, 88, 79 ,90, 70]
}

df = pd.DataFrame(data)

print(df)
# df.dropna(inplace=True)

# print(df)


# df.fillna(0, inplace=True)

# print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)

print(df)