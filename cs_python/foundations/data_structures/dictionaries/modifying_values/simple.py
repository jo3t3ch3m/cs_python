"""
To modify a value in a ditionary, givethe dictionary name,
followed by the key in square brackets and then the new value
you want associated with that key placed after the equal to sign( = ).

"""

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

### What Happened:
# First, we define a dictionary for alien_0 that contains only thealien's color.
# Then we change the value associated with the key 'color' to the value, 'yellow'.
# The output showswhat we changed, the alien has indeed changed from green to yellow.
