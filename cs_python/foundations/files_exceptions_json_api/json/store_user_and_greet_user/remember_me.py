# Python 2.7

# This is a simple program to store someone's username in a JSON file

##import json
##
##username = raw_input("What is your name? ")
##
##filename = 'username.json'
##with open(filename, 'w') as f_obj:
##    json.dump(username, f_obj)
##    print("\nGot it!")
##    print("We'll keep your name stored for when you come back, " + username.title() + "!")
    
# Now, let's write another program that will greet the username we just stored
# by using json.load()

####
####

# Editing the code to combine remember_me and greet_user in one file.
# So, the original code above will be commented, so we can still look to what we did earlier

##import json
##
### Load the username, if it has been stored previously.
###       Otherwise, ask the user for a name and store it
##filename = 'username.json'
##try:
##    with open(filename) as f_obj:
##        username = json.load(f_obj)
##
##except IOError:
##    username = raw_input("What is your name? ")
##    with open(filename, 'w') as f_obj:
##        json.dump(username, f_obj)
##        print("We'll keep your name stored for when you come back, " + username.title() + "!")
##else:
##    print("\nWelcome back, " + username + "!")

# The above code worked, except when you delete the JSON file,"FileNotFoundError is not defined"
# Python 2.7 uses "IOError" rather than "FileNotFoundError"

# https://github.com/philkr/lpo/commit/a1ee437ef46841d8f4d478a10d5eb26fb44c2433

# So the code works now. But, we've seen before when writing our programs,
# we might recognize that we can make our code better by breaking it up into
# a series of fucntions that perform specific jobs.
# This is called REFACTORING. This makes your code cleaner, easier to understand,
# and easier to expand.

# Let's Refactor the above the code to do just that

# REFACTORING

###
###

##import json
##
##def greet_user():
##    """Greet the user by their name."""
##    filename = 'username.json'
##    try:
##        with open(filename) as f_obj:
##            username = json.load(f_obj)
##
##    except IOError:
##        username = raw_input("What is your name? ")
##        with open(filename, 'w') as f_obj:
##            json.dump(username, f_obj)
##            print("We'll keep your name stored for when you come back, " + username.title() + "!")
##    else:
##        print("\nWelcome back, " + username + "!")
##
##greet_user()

# Because we are using a function now, we updated the comments with a docstring
# that shows how the program currently works.

# The code is a little cleaner, but the function greet_user() is doing more than
# just a greeting to the user... It is also retrieving a stored username if one exists
# and prompting for a new username if one doesn't exist.

# MORE REFACTORING
# refactor the greet_user() so it has less various tasks..
# Starting with moving the code for recovering a stored username to a separate function.
import json

def get_stored_username():
    """If available, get stored username."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username

def greet_user():
    """Greet the user by their name."""
    username = get_stored_username()
    if username:
        print("\nWelcome back, " + username + "!")

    else:
        username = raw_input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll keep your name stored for when you come back, " + username.title() + "!")

greet_user()

# This is good practice: a function should either return the value you're expecting,
# or it should return "None". This way, we can run a simple test
# with the return value of the function.

# However, we should factor one more block of code out greet_user()...
# If the username doesn't exist, we should move the code that prompts for a
# new username to a function dedicated to that purpose:

# ONE MORE REFACTOR

import json

def get_stored_username():
    """If available, get stored username."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
##    else:
##        return username

def get_new_username():
    """Prompt for a new username."""
    username = raw_input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by their name."""
    username = get_stored_username()
    if username:
        print("\nWelcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll keep your name stored for when you come back, " + username.title() + "!")

greet_user()

# Now, each of our functions have a clear purpose.
