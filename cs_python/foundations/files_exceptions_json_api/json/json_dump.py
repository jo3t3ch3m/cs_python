# Using json.dump() and json.load()

# Storing a set of numbers and another program that reads these number back into memory.

# First:
# json.dump()

# takes two arguments:
    # 1) a piece of data to store
    # 2) and a file object it can use to store the data

# Let's use json.dump() to store a list of numbers

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# So, the program ran, only it does not have any output
# After we run it, we'll see the numbers.json file in the same directory as this file.

