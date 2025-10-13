import pandas as pd
import matplotlib.pyplot as plt

data = {
    'col1' : [180000, 110, 18.9, 1400],  
    'col2' :     [360000, 905, 23.4, 1800],  
    'col3' : [540000, 1200, 45.6, 2000],
    'col4' : [720000, 1300, 67.8, 2500]
}

df = pd.DataFrame(data)
print(df)

df.plot(kind='bar')
plt.show()