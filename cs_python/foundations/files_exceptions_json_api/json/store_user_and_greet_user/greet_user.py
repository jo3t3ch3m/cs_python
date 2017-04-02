# Python 2.7

# This program will load data from the remember_me.py

import json

#username = raw_input("What is your name? ")

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("\nWelcome back, " + username.title() + "!")
    
# we used json.load() to read the information stored in username.json
# into the variable username. Then, the username is 'recovered', so we can welcome them back.

# But, we need to combine these two programs into one file. For, when someone
# runs remember_me.py, we want to get their username from memory.
# To do this, we'll use a "try" block that will try and recover the username.
# If the JSON file doesn't exist, we'll have the "except" block go ahead
# and request a username and store it in username.json for the next time.

# So go back to remember_me.py to add a few lines of code to display this...
