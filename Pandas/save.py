import pandas as pd


data = {
    "Name" : ["shlok" , "shreya", "shubham"],

    "Age" : [22,26,30],


    "City" : ["ranchi", "nagpur", "delhi",],

    
}


df = pd.DataFrame(data)


print(df)

# df.to_csv("output.csv", index=False) 

# df.to_excel("output.xlsx", index=False)


df.to_json("output.json" ,index=False)