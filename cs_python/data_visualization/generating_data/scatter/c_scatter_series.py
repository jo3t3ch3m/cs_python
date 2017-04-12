"""
Calculate Data Automatically

Writing out many lists by hand is inefficient.

Rather than passing our points in a list, we'll use a loop in Python
to do the calcualtions for us.

For example, let's try 100 points.

"""

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s = 40)


plt.title("Square Numbers", fontsize = 24)      # setting up title
plt.xlabel("Value", fontsize = 14)              # setting up x axis label
plt.ylabel("Square of Value", fontsize = 14)    # setting up y axis label


plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set up the range for each axis:
plt.axis([0, 1100, 0, 1100000])

plt.show()

