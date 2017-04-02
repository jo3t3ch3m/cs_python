# Python 2.7

# Example from Python Crash Course by Eric Matthes
# Using break to Exit a loop

# So far, we've looked at stopping a while loop by using a flag variable
# You can also use a BREAK statement...
# To exit a while loop immediately without running any remaining code in the loop,
# regardless of the results of any conditional test, use the break statement.

# The break statement directs the flow of your program
# You can use it to control which lines of code are executed and which aren't,
# so the program only executes code that you want it to, when you want it to
# Think of the term abstraction?

# Let's look at an example
# Consider a program that asks the user about places they've visited.
# To stop the while loop in this program by calling break as soon
# as the user enters the 'quit' value:

prompt = ("\nPlease enter the name of a city you have visited:")
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = raw_input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go " + city.title() + "!")

# this loop that starts with a "while True" will run continuously
# until it reaches a break statement

# You can use the break statement in any Python loops.
