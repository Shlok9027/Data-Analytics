import matplotlib.pyplot as plt


fig, ax = plt.subplots(1,2, figsize=(10,5))

x = [1,2,3,4,5,6]
y = [10,15,12, 20, 10, 30]


ax[0].plot(x,y)

ax[0].set_title("line plot")

ax[1].bar(x,y)

ax[1].set_title("Bar Chart")

plt.suptitle("Different Charts")


plt.tight_layout()

plt.show()