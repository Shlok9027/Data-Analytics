import matplotlib.pyplot as plt


regions = ['north', 'south', 'east', 'west' ]

values = [3000,4500, 2000, 1500]

plt.pie(values, labels=regions, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red'])


plt.title("values of regions")
plt.show()