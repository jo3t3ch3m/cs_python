# Python 2.7

# starting dictionary
joe = {
    'favorite_food': 'spaghetti',
    'favorite_color': 'orange',
    'lucky_number': '7'
    }

# Acessing the dicitonary

# returning the whole dictionary:
print joe

# accessing the value by calling the key:
print(joe['favorite_color'])
print(joe['lucky_number'])

# Adding New Key-Value Pairs
# just give the name of the dictionary followed by the new key in square brackets
# along with the new value
joe['mobile_phone'] = '757-784-5555'

print(joe)

# Removing Key-Value Pairs
# Sometimes you no longer need a piece of information that is stored in a dictionary.
# You can use the "del" statement to remove the key-value pair.
# This statement just needs the name of the dictionary and the key you want to remove.
del joe['favorite_food']

print joe
