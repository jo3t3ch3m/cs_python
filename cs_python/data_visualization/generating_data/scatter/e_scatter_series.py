"""
Removing Outlines from Data Points

matplotlib allows you to color points individually in a scatter plot.
When plotting points, the two default colors can seem to blend. To remove
outlines around the points, pass the argument edgecolor = 'none' when
you call scatter()

Using a Color Map

a colormap is a series of colors in a gradient that moves from a starting
to ending color.

"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# change the color of the points
# with an RGB model:
plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues,
            edgecolor = 'none', s = 40)


plt.title("Square Numbers", fontsize = 24)      # setting up title
plt.xlabel("Value", fontsize = 14)              # setting up x axis label
plt.ylabel("Square of Value", fontsize = 14)    # setting up y axis label


plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set up the range for each axis:
plt.axis([0, 1100, 0, 1100000])

plt.show()

