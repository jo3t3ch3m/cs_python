# Python 2.7

# RETURNING A DICTIONARY
# a function can return any value you need it to, including more complex
# data structures like lists and dictionaries.

# For example, following similar format like the formatted name program:

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# the function takes in a first and last name, and packs these values into a dictioanry.
# The value of first_name is stored with the key 'first', and the value of last_name
# is stored with the key 'last'.
# The entire dictionary representing the person is returned.
# The return value is printed with the original two pices of tectual info. now stored
# in a dictionary.

