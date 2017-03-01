# Python 2.7

name = "ada lovelace"
print(name.title())

# Above we stored the value, "ada lovelace" in a variable named, 'name'
# The dot (.) after name in name.title() tells Python to make the title() method
# act on the variable, name.

# CONCATENATING STRINGS/COMBINING STRINGS

# While we program more and more, we'll find that it is useful for us to combine strings
# for example, let's say we wanted to combine to seperate variables,
# like first name and last name.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# or with a little more content and use of variables:
message = "Hello " + full_name.title() + "!"
print(message)


