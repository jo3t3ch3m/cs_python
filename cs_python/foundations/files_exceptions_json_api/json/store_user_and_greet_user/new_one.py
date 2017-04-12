import json

def get_stored_username():
    """If available, get stored username."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = raw_input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by their name."""
    username = get_stored_username()
    if username:
        print("\nWelcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll keep your name stored for when you come back, " + username.title() + "!")

greet_user()
