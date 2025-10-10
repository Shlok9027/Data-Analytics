import matplotlib.pyplot as plt


month = [1,2,3,4,5,6]

sales = [1000, 2300, 1500, 7800, 3500, 3400]

plt.plot(month, sales)

plt.plot(month, sales, color="blue", linestyle="--", marker="o", label='2025 sales data')

plt.xlabel("Months")
plt.ylabel("Sales in INR")
plt.title("Sales data of 2025")
plt.legend(loc='upper left', fontsize=15)


plt.grid(color='green', linestyle=':', linewidth=0.5)


plt.xlim(0,7)
plt.ylim(0,8000)

plt.xticks([1,2,3,4,5,6],["Jan","Feb","Mar","Apr","May","Jun"])
plt.yticks([0,1000,2000,3000,4000,5000,6000,7000,8000])


plt.show()