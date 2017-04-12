"""
Plotting and Styling Individual Points with scatter()

Sometimes it's useful to be able to plot and style individual points
based on certain characteristics.

For Example, you might plot small values in one color and larger values
in a different color.

You could also plot a large data set with one set of styling options
and then emphasize individual points by replotting them with different options.

To plot a single point, use the scatter() function. Pass the single (x, y)
values of the point of interest to scatter(), and it should plot those values

"""

import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize = 24)      # setting up title
plt.xlabel("Value", fontsize = 14)              # setting up x axis label
plt.ylabel("Square of Value", fontsize = 14)    # setting up y axis label

# Set size of tick labels.
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

