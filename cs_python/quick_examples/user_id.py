"""
the get() method on dictionaries

"""

user_id_to_name = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
    }

def greeting(user_id):
    return "Hi %s!" % user_id_to_name.get(user_id, 'there')

print(greeting(382))

print(greeting(123))
