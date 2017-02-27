# Python 2.7
# 5

# Passing Arguments

# The definition for a function can have several parameters,
# because of this, a function call may need several arguments.

# There are several ways to pass arguments to your functions...
    # Positional Arguments
        # need to be in the same order the parameters were written
    # Keyword Arguments
        # where each argument consists of a variable name and a value;
        # and lists and dictionaries of values

# POSITIONAL ARGUMENTS

# When a function is called, Python matches each argument in the function call
# with a paremeter in the definition of a function.
# The simplest way is to base it on the order of arguments provided (hence, positional)
# Values matched up this way are positional arguments.

# Consider a function that shows info about macroinvertebrates(or bugs)

def describe_bug(bug_type, bug_name):
    """Display information about a macroinvertebrate"""
    print("\nI collected a " + bug_type + ".")
    print("This " + bug_type + "'s name is " + bug_name.title() + ".")

describe_bug('dragonfly larvae', 'anisoptera')

# The definition shows that this function needs a type of   
