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
    print("This " + bug_type + "'s order is " + bug_name.title() + ".")

describe_bug('dragonfly larvae', 'anisoptera')

# The definition shows that this function needs a type of bug and the bug's name.

# Multiple Function Calls
# You can call a function as many times as needed. Describing a second,
# different bug requires just one more call to describe_bug():

describe_bug('stonefly', 'plecoptera')
# In this second function call, we pass describe_bug() the arguments
# 'stonefly' and 'plecoptera'. Just like the previous arguments,
# Python matches 'stonefly' with the parameter bug_type and 'plecoptera'
# with the parameter bug_name.

# Just like before, the function executes its task.

# Calling a function more than once is very efficient. The code only needs to
# be written once in the function. Anytime you want to describe a newly collected
# bug, you just call the function with the new bug's information.

# The order matters!!!
# of course, order matters in positional arguments.
# For example, if we reordered decribe_bug(bug_type, bug_name) to
# decribe_bug(bug_name, bug_type), we might get a funny answer. Try it!







