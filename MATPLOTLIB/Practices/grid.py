import matplotlib.pyplot as plt

import numpy as np


x  = np.linspace(0.0, 0.5)
y = np.cos(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots(1,2,figsize=(10,4))

ax[0].plot(x, y, 'b-')
ax[0].set_title('Default Grid')

ax[1].plot(x, y, 'b-')
ax[1].set_title('Customized Grid')

ax[1].grid(True)

plt.show()