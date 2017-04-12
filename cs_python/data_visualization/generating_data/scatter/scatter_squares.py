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

plt.scatter(2, 4)

plt.show()

