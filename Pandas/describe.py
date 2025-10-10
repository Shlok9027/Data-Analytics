import pandas as pd
data  = {
    "Name" : ["Shlok" , "Shreya", "Shubham" , "Ankit" , "Ankita"],

    "Age" : [22, 26, 30, 37, 24],

    "Salary" : [45000, 50000, 70000, 49000, 55000],

    "Performace_Score" : [97 , 88, 79 ,90, 70]





}

df = pd.DataFrame(data) 

print(df)

# print(df.info())

print("Discriptive Statics")


print(df.describe())
