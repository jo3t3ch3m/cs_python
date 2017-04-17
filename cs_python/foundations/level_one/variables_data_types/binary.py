"""

Directions: Make each letter of your name a variable in Python.
            Make the value for each letter in your name the correct
            binary number associated with it.

            Then, have Python return your name in plain english and
            in binary, using the variables you just made!

"""

# Telling Python the Binary number associated with each letter
J = '01001010 '
O = '01001111 '
S = '01010011 '
E = '01000101 '
F = '01000110 '

S = '01010011 '
I = '01001001 '
L = '01001100 '
R = '01010010 '
# (We don't need to redefine the same letters)

first_name = "joe"
last_name = "seiler"

full_name = first_name + " " + last_name

print("Here is my first name coded in binary:")
print(J + O + S + E + F)

print("\nHere is my last name coded in binary:")
print(S + E + I + L + E + R)

print("\nHere is my full name is plain english:")
print(full_name.title())
