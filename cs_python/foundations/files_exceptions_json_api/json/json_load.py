# now, for the json.load() function

# this program uses json.load() to read back the list into memory



import json

filename = 'numbers.json'       # we make sure to read from the same file we wrote to
with open(filename) as f_obj:   # we open it in read mode
    numbers = json.load(f_obj)

print(numbers)

# the json.load() function loads the info stored in numbers.json

# This is a simple way to share data between two programs
