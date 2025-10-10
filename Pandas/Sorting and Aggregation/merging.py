import pandas as pd

df_orders = pd.DataFrame({
    "OrderId" : [1, 2, 3, 4],
    "Product": ["Mobile", "Laptop","HeadPhone", "Pen"],

})

df_customers  =pd.DataFrame({
    "OrderId" : [1,2,3,5],
    "Names" : ["Shlok", "Shreya", "Shubham", "Aniket"]


})


df_merge = pd.merge(df_orders,df_customers , on='OrderId', how='right')

print("inner merge")

print(df_merge)