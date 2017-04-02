# Python 2.7
# 4

# Arguments and Parameters

# In the function before, we defined it to require a vlaue for the variable, username
# Once we called the function and gave it the info (person's name), it correctly printed the greeting.

# The variable, username in the function's definition is anexample of a PARAMETER.
# A Parameter is a piece of information the function needs to execute its task.

# The value, 'timmy' in greet_user('timmy') is an example of an ARGUMENT.
# An Argument is a piece of information that is passed from a function call to a function.

# For example, let's change up the code slightly and see what happens!

def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")
# GO ahead and call the function with an empty parentheses.
greet_user()

# We'll get an error...
# TypeError: greet_user() takes exactly 1 argument (0 given)

# This is because we omitted the information needed for the function to do its job correctly
# It is waiting for the information to be provided.
