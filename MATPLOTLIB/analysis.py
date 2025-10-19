# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 2, 3, 4])  # X-axis 
# y = x*2  # Y-axis

# plt.plot(x, y)  
# plt.show()

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.figure(figsize=(6, 4))
# plt.plot(x, y, marker='o', linestyle='-')

# # Add annotations
# for i, (xi, yi) in enumerate(zip(x, y)):
#     plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

# plt.title('Line Chart with Annotations')
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')

# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np


# x = np.array([1,2,3,4
# ])

# y = x*2

# plt.plot(x,y)
# plt.xlabel('X - Axis')

# plt.ylabel('Y - Axis')

# plt.title('PLOT')
# # plt.show()/

# # plt.figure()

# x1 = [2, 4, 6, 8]
# y1 = [3, 5, 7, 9]


# plt.plot(x1,y1,'-.')

# plt.fill_between(x,y,y1,color='purple',alpha=0.5)

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# fruits = ['Apple', 'Orange', 'Mango', 'Lemon', 'Kasmiri Apple']
# sales = [400, 800, 360, 1000, 400]

# plt.bar(fruits, sales)
# plt.title('Sales Report')
# plt.xlabel('fruits')
# plt.ylabel('Sales per year')
# plt.tight_layout()


# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
# sales = [400, 350, 300, 450]

# plt.bar(fruits, sales, color='violet')
# plt.title('Fruit Sales')
# plt.xlabel('Fruits')
# plt.ylabel('Sales')
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd

# fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
# sales = [400, 350, 300, 450]

# plt.barh(fruits,sales, color='black')
# plt.title('Fruit Sales')
# plt.xlabel('Fruits')
# plt.ylabel('Sales')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# barwidth = 0.25
# fig = plt.subplots(figsize=(8,6))

# CSE = [12, 54, 2, 56, 323]
# AIML = [34, 64, 31, 23, 31]
# DATA_SCIENCE = [43, 23, 6, 45, 76]

# br1 = np.arange(len(CSE))
# br2 = [x + barwidth for x in br1]
# br3 = [x + barwidth for x in br2]

# plt.bar(br1, CSE, color='r', width=barwidth, edgecolor='grey', label='CSE')
# plt.bar(br2, AIML, color='g', width=barwidth, edgecolor='grey', label='AIML')
# plt.bar(br3, DATA_SCIENCE, color='b', width=barwidth, edgecolor='grey', label='DATA SCIENCE')

# plt.xlabel('Year', fontweight='bold', fontsize=15)
# plt.ylabel('Students Passed', fontweight='bold', fontsize=15)
# plt.xticks([r + barwidth for r in range(len(CSE))],
#            ['2015', '2016', '2017', '2018', '2019'])

# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy  as np

# x = np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
# y = np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])


# plt.scatter(x,y)
# plt.title('Scatter Graph')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy  as np

# x1 = np.array([160, 165, 170, 175, 180, 185, 190, 195, 200, 205])
# y1 = np.array([55, 58, 60, 62, 64, 66, 68, 70, 72, 74])

# x2 = np.array([150, 155, 160, 165, 170, 175, 180, 195, 200, 205])
# y2 = np.array([50, 52, 54, 56, 58, 64, 66, 68, 70, 72])

# plt.scatter(x1, y1, color='blue', label='Group 1')
# plt.scatter(x2, y2, color='red', label='Group 2')

# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.title('Comparison of Height vs Weight between two groups')
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy  as np



# x1 = np.array([160, 165, 170, 175, 180, 185, 190, 195, 200, 205])
# y1 = np.array([55, 58, 60, 62, 64, 66, 68, 70, 72, 74])
# z1 = np.array([53, 28, 87, 52, 94, 36, 58, 50,52, 89])

# x2 = np.array([150, 155, 160, 165, 170, 175, 180, 195, 200, 205])
# y2 = np.array([50, 52, 54, 56, 58, 64, 66, 68, 70, 72])
# z2 = np.array([55, 58, 60, 62, 64, 66, 68, 70, 72, 74])

# plt.scatter(x1, y1, color='blue', label='Group 1')
# plt.scatter(x2, y2, color='red', label='Group 2')
# plt.scatter(z1, z2, color='red', label='Group 2')

# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.title('Comparison of Height vs Weight between two groups')
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt 
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [30, 80, 150, 200, 300]  # Bubble sizes

plt.scatter(x, y, s=sizes, alpha=0.5, edgecolors='blue', linewidths=2)
plt.title("Bubble Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
