# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 2, 3, 4])  # X-axis 
# y = x*2  # Y-axis

# plt.plot(x, y)  
# plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-')

# Add annotations
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

plt.title('Line Chart with Annotations')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

plt.grid(True)
plt.show()