# Python 2.7

# Let's use the int() function in another program
# What if we needed a program that determines whether a person is tall enough
# to ride a certain roller coaster:

height = raw_input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride this coaster wehn you're a little older")
    
# MAIN IDEA: when you use numerical input to do calcualtions and comparisions,
# be sure to convert the value of the input to a numerical representation first




