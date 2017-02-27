# Python 2.7
# 3

# Passing Data(or information) to a Function

# We can bolster our last function we used to do a little more.
# We'll have the task of the function greet the user by their name.

# How do we do this?

# Before, we left the parentheses in the function definition empty. Now,
# we'll enter "username" in the parentheses of the function's definition.

# When we add the username we'll allow the function to accept any value of
# "username" we specify. So, the function will now expect you to provide
# a value for "username" every time it is called.

# When we call greet_user(), we can throw it a name, inside of the parentheses.

def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

greet_user('timmy')
# by writing greet_user('timmy'), this calls the function and provides the information
# the function needs in order to execute the print statement.

# Since our last lesson left off with user input..

# How can have the defintion take whatever the user types in??

####
####

def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

username = raw_input("What is your name? ")
greet_user()
