# Python 2.7

# a function that takes a first and last name, and returns a neatly
# formatted full name.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

print(musician)

# The definition of get_formatted_name() takes two parameters, first and last name

# THe function combines these two names, adds a space between them,
# and stores the result in full_name.

# When you call a function that returns a value, you need to provide a variable
# where the return value can be stored. In this case, musician

