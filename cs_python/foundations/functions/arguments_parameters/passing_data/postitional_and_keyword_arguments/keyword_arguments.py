# Python 2.7
# 6

# More Passing Arguments

# The definition for a function can have several parameters,
# because of this, a function call may need several arguments.

# There are several ways to pass arguments to your functions...
    # Positional Arguments
        # need to be in the same order the parameters were written
    # Keyword Arguments
        # where each argument consists of a variable name and a value;
        # and lists and dictionaries of values

# KEYWORD ARGUMENTS
# a name-value pair that you pass to a function. You directly associate the name
# and the value within the argument, so when you pass to the function,
# there is no confusion. Keyword arguments allow free you from having to worry
# about the correct order of your arguments in the function call. 

# Consider the function from our previous example, showing info about macroinvertebrates(or bugs)

def describe_bug(bug_type, bug_name):
    """Display information about a macroinvertebrate"""
    print("\nI collected a " + bug_type + ".")
    print("This " + bug_type + "'s order is " + bug_name.title() + ".")

describe_bug(bug_type= 'dragonfly larvae', bug_name= 'anisoptera')

# The function describe_bug() has not changed.
# When we call the function, we clearly state which parameter each argument
# should be matched with. When Python reads the function call, it knows to store
# the argument 'dragonfly larvae' in the parameter bug_type and the argument 'anisoptera'
# in bug_name. The output correctly displays that we have a dragonfly larvae
# of the order 'anisoptera'.

# Unlike positional arguments,the order of keyword arguments is no matter,
# because Python knows where each value should go.









