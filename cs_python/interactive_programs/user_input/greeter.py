# Python 2.7

# The input() function, or raw_input() takes one argument: the prompt
# or instructions, that we want to display to the user so they know what to do.

# NOTE: Though this is originally written in 2.7, I will refer to raw_input() as input()

# IMPORTNANT: WRITE CLEAR PROMPTS!
# Each time you use the input() function, you should include a clear, easy-to-follow
# prompt that tells the user exactly what kind of inforamtion you're looking for.

# Write a program that asks for the user's name, then have the
# exact name they typed in return to the user.

##################################################
##################################################

####name = raw_input("Please enter your name: ")
####print("Hello, " + name + "!")

# Sometimes you'll want to write a longer prompt, perhaps more than one line
# For example, you might want to tell the user why you're asking for certain input

# You can store your prompt in a variable and pass that variable to the input() function
# This allows you to build your prompt over several lines,
# then write a clean input() statement
# Remember, think of a statement as a complete thought

prompt = "If you tell us who you are, we can create a unique message for you to see."
prompt += "\nWhat is your first name? "

name = prompt = raw_input(prompt)
print("\nHello, " + name + "!")

# This example shows another way to build a multi-line string.
# The first line stores the first part of the message in the variable, prompt
# In the next line, the operator, += takes the string that was stored in prompt
# and adds the new string onto the end

# As you can see, the prompt now spans two lines, with a space after the question mark for clarity.


