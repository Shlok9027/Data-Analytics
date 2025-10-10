import pandas as pd 

data  = {
    "Name" : ["Shlok" ,None, "Shreya", "Shubham" , "Ankit" , "Ankita"],

    "Age" : [22,None, 26, 30, 37, 24],

    "Salary" : [45000,None, 52000, 70000, 49000, 55000],

    "Performace_Score" : [97 , None,88, 79 ,90, 70]


}

df = pd.DataFrame(data)

print(df)


print(df.isnull().sum())