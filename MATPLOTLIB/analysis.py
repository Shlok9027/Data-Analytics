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



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

barwidth =  0.25
fig = plt.subplots(figsize=(12,8))

CSE = [12,54,2,56,323,1,433]
AIML = [34,64,31,23,31,2, 21]
DATA_SCIENCE = [43,23,6,45,766,345]


br1 = np.arange(len(CSE))
br2 = [x + barwidth for x in br1]
br2 = [x + barwidth for x in br2]

plt.bar(br1, CSE, color = 'r', width=barwidth, edgecolor = 'grey', label='CSE')

plt.bar(br2, AIML, color = 'g', width= barwidth, edgecolor = 'grey', label='ECE')

plt.bar(bar3, DATA_SCIENCE, color = 'b')