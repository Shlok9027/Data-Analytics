import matplotlib.pyplot as plt


products = ["a","b","d","e","f" ]

sales = [100, 500, 350, 210, 350]

plt.bar(products,sales , color="green" , width=0.5 , label='Sales data')

plt.xlabel("Products" )
plt.ylabel("Sales in INR")
plt.title("Sales data of products")
plt.legend(loc='upper right', fontsize=15)
plt.show()