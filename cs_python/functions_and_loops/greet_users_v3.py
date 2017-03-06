# Python 2.7

# PASSING A LIST    

# In this class, you'll find it useful to pass a list to a function,
# whether it's a list of items, or more complex object, such as dictionaries.

# When you pass a list to a function, the function gets direct access to the contents
# of the list. Let's use functions to make working with lists more efficient.

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['albert', 'bart', 'watson']
greet_users(usernames)
        
