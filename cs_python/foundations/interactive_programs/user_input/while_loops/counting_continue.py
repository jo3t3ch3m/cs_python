# Python 2.7
# Example from Python Crash COurse By Eric Matthes

# Using continue in a loop

# Instead of breaking out of a loop entirely without executing the rest of its code,
# you can use the "continue" statement to return to the beginning of the loop
# based on the result of a conditional test.
# Let's look at a modified version of our previous example, counting.py

# Here, this is a loop that counts from 1 to 10 but prints
# only the odd numbers in that range:

current_number = 0 # we start counting from 1
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0:     # This if statement checks the modulo of current_number and 2
        continue                    
# If the modulo is indeed 0, the continue statement tells Python to ignore
# the rest of the loop and return to the beginning.
# If not, then the loop is stopped and Python prints the current number
    print(current_number)
