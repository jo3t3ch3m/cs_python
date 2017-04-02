# Python 2.7
# 2

def get_name(first_name, last_name):
    print("Hello User!")
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = raw_input("First name: ")
    l_name = raw_input("Last name: ")

    name = get_name(f_name, l_name)
    print("\nHello, " + name + "!")




