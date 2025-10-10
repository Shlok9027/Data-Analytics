import pandas as pd


data  = {
    "Name" : ["Shlok" , "Shreya", "Shubham" , "Ankit" , "Ankita"],

    "Age" : [22, 26, 30, 37, 24],

    "Salary" : [45000, 52000, 70000, 49000, 55000],

    "Performace_Score" : [97 , 88, 79 ,90, 70]


}

df = pd.DataFrame(data)

print(df)


# print(df[["Salary", "Age"]])

# One condition

"""filtered_row = df[df["Salary"] > 50000]

print(filtered_row)"""


# more than one condition



filtered_row = df[(df["Salary"] > 49000) & (df["Age"] > 29)]


print("age more than 30 with salary more than 50000")
print(filtered_row)




filtered_row = df[(df["Salary"] > 49000) | (df["Age"] > 29)]

print("age more than 30 or salary more than 50000")
print(filtered_row)