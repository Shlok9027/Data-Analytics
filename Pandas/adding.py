# import pandas as pd

# data  = {
#     "Name" : ["Shlok" , "Shreya", "Shubham" , "Ankit" , "Ankita"],

#     "Age" : [22, 26, 30, 37, 24],

#     "Salary" : [45000, 52000, 70000, 49000, 55000],

#     "Performace_Score" : [97 , 88, 79 ,90, 70]


# }


# df = pd.DataFrame(data)

# print(df)
# # add new column

# df["Bonus"] = df['Salary' ] * 0.1

# print(df)


# df.insert(5, "rating" ,[8,5,7,4,9])

# print(df)


import pandas as pd
data  = {
    "Name" : ["Shlok" , "Shreya", "Shubham" , "Ankit" , "Ankita"],

    "Age" : [22, 26, 30, 37, 24],

    "Salary" : [45000, 52000, 70000, 49000, 55000],

    "Performace_Score" : [97 , 88, 79 ,90, 70]


}

df = pd.DataFrame(data)


print(df)

df["increment"] = df["Salary"] * 0.15

print(df)

df.insert(5,"Ranking" , [1,3,2,8,2])

print(df)

df.loc[0,"Salary"] = 500000

print(df)