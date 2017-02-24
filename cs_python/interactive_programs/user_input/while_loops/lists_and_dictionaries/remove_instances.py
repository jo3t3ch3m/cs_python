# Python 2.7

# The following example is a rendition from Python Crash Course by Eric Matthes
# The transect example is inspired by my experience in field biology

# Remember, if we want to remove an item from a list, we use the remove() function.
# This worked, because the value we wanted to remove only appeared once in the list.

# Let's say you had a list of different kinds of trees with the value 'red maple'
# repeated several times.
tree_types = ['yellow poplar', 'loblolly', 'red maple', 'black gum', 'red maple', 'yellow poplar']
print(tree_types)

tree_types.remove('red maple')
print(tree_types)

# This does what we want. But, you can see Python only removes the first instance of the value, 'red maple'
# and "leaves" the rest.

# To remove all instances of that value,
# you can run a while loop until 'red maple' is no longer in the list:

# transect.py

tree_types = ['yellow poplar', 'loblolly', 'red maple', 'black gum', 'red maple', 'yellow poplar']
print(tree_types)

while 'red maple' in tree_types:
    tree_types.remove('red maple')

print(tree_types)

# We start with a list containing multiple instances of 'red maple'.
# After printing the list, Python enters the while loop because it finds the 
# item 'red maple' in the list more than once. Once inside the loop, Python
# removes the first instance of 'red maple', returns to the line with while, and then
# reenters the loop when it finds that 'red maple' is still in the list.
# Python removes each instance of 'red maple' until the value is no longer
# contained in the list, then Python exits the loop and prints the list again
