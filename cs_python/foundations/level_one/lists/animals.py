import random

animals = ['jaguar', 'elephant', 'parrot']

print("\nShowing everything in the list so far:")
print(animals)

# lists are 0-based
# remember when we compared decimal numbers to binary numbers?
    # We start at the number, 0
    # This is the same when counting in Python

# Acessing Elements in a List
print("\nFirst item in the list:")
print(animals[0])

print("\nFirst item in the list, starting with a capital letter:")
print(animals[0].title())

# Using individual Values from a List
message = "My first animal was a " + animals[0].title() + "."

print(message)

# Changing the items in a list

animals[0] = 'lion'

print(animals)

# Adding items to the list
animals.append('giraffe')

print(animals)

random.choice(animals)
