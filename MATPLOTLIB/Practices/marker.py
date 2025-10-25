import matplotlib.pyplot as plt
import numpy as np

x = [0,3,6,1,  5,  0]
y = [0,6,0,3.5,3.5,0]

plt.plot(x, y, marker='o', linestyle='-', color='blue',label='Data Line',)

plt.title('Line Plot with Markers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()