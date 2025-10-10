import matplotlib.pyplot as plt


scores = [23, 45, 56, 78, 89, 90, 34, 23, 45, 67, 89, 90, 34, 23, 45, 67, 89]

plt.hist(scores, bins=5, color='purple', edgecolor='black')

plt.xlabel("Scores")
plt.ylabel("Number of Students")

plt.title("Distribution of Student Scores")

plt.show()
