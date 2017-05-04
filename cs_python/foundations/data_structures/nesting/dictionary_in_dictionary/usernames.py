# Python 2.7
# example from Python Crash Course by Eric Matthes
# Sure, you can nest a dictionary inside of another dictionary,
# But, your program can potentially get complicated, really quickly

# For example, let's say you run a website containing several users,
# each with a unique username. You can use the usernames as the keys in the dictionary
# You can store info. about each user by using a dictionary as the value
# associated with their username

# In this example, we'll store three pieces of info. about each user:
    # first name
    # last name
    # location

# We'll access this info. by looping through the usernames and the dictionary
# of info. associated with each username:

# many_users.py

# First, we'll define a dictionary called "users" with two keys: one each for the usernames
# The value associated with each key is a dictionary that includes each user's
# first name, last name, and location.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
# Looping through the users dictionary
# Python stores each key in the variable "username", and the dictionary associated
# with each username goes into the variable "user_info".

for username, user_info in users.items():
    print("\nUsername: " + username)            # Once inside the main dictioanry loop, we print the username
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Notice each user's dictionary structure is identical.
# This helps with making the code less complicated and easier to work with.
# If each the dictioanry for each user had different keys, the code inside the
# for loop would be a lot more complicated!


