# Python 2.7

# When you use the input() function, Python interprets everything the user enters
# as a string. Consider the next interpreter session, where the computer asks for the user's age:

age = raw_input("How old are you? ")
print(age)

# This seems fine at first, but Python returns the string representation
# of the number entered by the user

# If all you want to do is print the input, this works well.
# However, if you try to use the input as a number, you'll get an error.
# When you try to use the input to do a numerical comparison,
# Python won't like it, because it can't compare a string to an integer.
# For example,
# age >= 18
# the string typed in can't be compared to the numerical value 18.

# We can fix this by using the int() function, which tells Python to treat
# the input as a numerical value.
# The int() function converts a string representation of a number to a numerical representation

age = raw_input("How old are you? ")
age = int(age)
print(age >= 18) # if you try this in the interpreter, omit the print() function




