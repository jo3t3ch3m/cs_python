"""

Saving Your Plots Automatically
If you want your program to automatically save the plot to a file,
you can replace the call to plt.show() with a call to plt.savfig()

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

# Automatic Save
plt.savefig('squares_plot.png', bbox_inches='tight')

