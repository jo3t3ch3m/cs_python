# Python 2.7

# When you define a function, you can define a default value for each parameter
# So, if an argument for a paremeter is provided in the function call,
# Python uses the argument value. Otherwise, it uses's the default value

# Default Value Purpose:
# they can simplify the function calls and clarify ways in whichthe functions are used.

# For exmaple, when you notice a pattern. For instance, in the describe a bug program,
# you may notice that most of the calls are being used to describe a certain bug (of course!)
# We can set the default value of bug_type to 'stonefly'.
# This way, anyone calling the describe_bug() for a stonefly can omit that info.



def describe_bug(bug_name, bug_type='stonefly'):
    """Display information about a macroinvertebrate"""
    print("\nI collected a " + bug_type + ".")
    print("This " + bug_type + "'s order is " + bug_name.title() + ".")

describe_bug(bug_name = 'plecoptera')
