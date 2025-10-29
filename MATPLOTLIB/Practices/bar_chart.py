import matplotlib.pyplot as plt


def add_label(x,y):
    for i in range(len(x)):
        plt.text(i, y[i] //2, y[i], ha='center', va='bottom',
                 bbox=dict(facecolor='white', edgecolor='black', pad=2.0));


x = ['B.Tech', 'M.Tech', 'B.Sc', 'M.Sc', 'Phd']

y = [32034, 12034, 23045, 15000, 5000]

plt.bar(x, y)

add_label(x, y)

plt.title('Number of Students in Various Courses')
plt.xlabel('Courses')
plt.ylabel('Number of Students')

plt.show()