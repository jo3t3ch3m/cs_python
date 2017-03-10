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

import json

# Load the username, if it has been stored previously.
#       Otherwise, ask the user for a name and store it
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

except FileNotFoundError:
    username = raw_input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll keep your name stored for when you come back, " + username.title() + "!")
else:
    print("\nWelcome back, " + username + "!")

# The above code worked, except when you delete the JSON file,"FileNotFoundError is not defined"

        
