import matplotlib.pyplot as plt

import seaborn as sns

 
 
import numpy as np 

import pandas as pd


data = pd.read_csv('Data_Visualization/vgsales.csv')

print(data.head())
print(data.tail())


# print(data.columns)
# print(data.isnull().sum())
#Removing 4th indexed value from the dataframe
# print(data.drop(4).head())
# x = [0,1,2]
# y = [3,5,9]

# plt.plot(x,y)

# plt.show()

# print(data['Genre'].unique())


# print(data['Genre'].value_counts())

# #  Bar Chart Using Matplotlib
# print("\n")
# x_bar = data['Genre'].value_counts().index
# print(x_bar)

# print('\n')
# y_bar = data['Genre'].value_counts().values
# print(y_bar)

# plt.figure(figsize=(10,6))

# plt.xticks(rotation=350, fontsize=10, fontstyle='italic')

# plt.xlabel('Genre', fontsize=15)
# plt.ylabel('count', fontsize=15)

# plt.suptitle('Bar Chart of Genre', fontsize=20)

# plt.bar(x_bar, y_bar, width=0.5, color='purple')

# plt.show()

# Bar Chart Using Seaborn

# sns.countplot(x='Genre', data=data, order=data['Genre'].value_counts().index, color='purple')

# plt.show()

# sales_data = data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

# print(sales_data)

# region_sales= sales_data.T.sum(axis='columns')

# print(region_sales) 


# plt.pie(region_sales, labels=region_sales.index,startangle=90,explode=(0.2,0,0,0), autopct='%1.1f%%', colors=['blue','orange','yellow','pink'])
# plt.title('Total Sales acroos various region')
# print(data.describe())
# plt.show()
# plt.hist(data['Year'], color='purple')

# plt.show()


# counts, bins, _= plt.hist(data['Year'], bins=40)

# # print(bins)

# plt.show()

# sns.kdeplot(data['Year'])
# plt.show()   

plt.figure(figsize=(8,5))

sns.boxplot(y=data['Global_Sales'])
plt.yticks(fontsize=15)
plt.show()