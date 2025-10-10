import pandas as pd

data = {
    "Time" : [1,2,3,4,5,6,7,8,9,10,11,12],
    "Value" : [22,3,None,72,32,None,74,35,66,None,48,74]
}


df =  pd.DataFrame(data) 

print(df)