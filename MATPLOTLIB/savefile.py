import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y =[10,15,20,25,30]

plt.plot(x,y, color='blue', marker='o' )



plt.title("Simple Line Plot")

plt.xlabel("X axis")

plt.ylabel("Y axis")


plt.savefig("line_plot.png",dpi=300, bbox_inches='tight', )

plt.show()
