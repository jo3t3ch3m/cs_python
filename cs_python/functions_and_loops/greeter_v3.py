# Python 2.7

# USING A FUNCTION WITH A WHILE LOOP

# Let's use the get_formatted_name() function we looked at earlier
# Only this time, we'll throw in a while loop to greet users more formally.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your first name:")
    print("(enter 'q' at any time to quit)")

    f_name = raw_input("First name: ")
    if f_name == 'q':
        break
    l_name = raw_input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

    
