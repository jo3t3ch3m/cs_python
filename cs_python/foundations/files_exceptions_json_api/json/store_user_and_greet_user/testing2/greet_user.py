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


