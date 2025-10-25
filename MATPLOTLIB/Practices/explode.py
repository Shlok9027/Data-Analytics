
import matplotlib.pyplot as plt
import numpy as np

# Car names
cars = ['BMW', 'AUDI', 'FORD', 'TESLA', 'HONDA', 'TOYOTA']

# Corresponding sales data
data = [354, 322, 243, 325, 265, 299]

# Explode certain slices outward for emphasis
# Values represent fraction of the radius (e.g., 0.1 = 10%)
explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)

# Colors for each slice
colors = ['red', 'blue', 'beige', 'orange', 'purple', 'yellow']

# Green border around each wedge
wp = {'linewidth': 1, 'edgecolor': 'green'}

# # Function to format percentage + actual value
# def func(pct, allvalues):
#     absolute = int(pct / 100. * np.sum(allvalues))
#     return "{:.1f}%\n({:d} g)".format(pct, absolute)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Create pie chart
wedges, texts, autotexts = ax.pie(
    data,
    autopct="%1.1f%%",
    explode=explode,
    labels=cars,
    shadow=True,
    colors=colors,
    startangle=90,        # start from the top
    wedgeprops=wp,
    textprops=dict(color="magenta"),
    counterclock=True     # pie slices drawn anti-clockwise (default)
)

# Add legend to the side
ax.legend(
    wedges,
    cars,
    title="Cars",
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Customize label appearance
plt.setp(autotexts, size=8, weight="bold")

# Title of the chart
ax.set_title("Car Sales Distribution")
plt.savefig('pie_chart.png')
# Display chart
plt.show()
