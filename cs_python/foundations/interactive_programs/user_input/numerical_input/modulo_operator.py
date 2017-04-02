# Python 2.7

# For this example, open up Python's interpreter

# A useful tool for working with numerical inforamtion is the MODULO operator(%)
# This divides one number by another number and returns the remainder:

# in the interpreter type the following:
#       >>> 4 % 3

#       >>> 5 % 3

# try out a few other examples of your own!

# The modulo operator doesn't tell you how many times one number fits into another;
# it just tells you what the remainder is.
# When one number is divisible by another number, the remainder is 0,
# so the modulo operator always returns 0.
# You can use this fact to determine if a number is even or odd:

number = raw_input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# How does this work?
# Even numbers are always divisble by two, so if the modulo of a number and two
# is zero, the number is even. Otherwise, it's odd.
# Simple, Right?




