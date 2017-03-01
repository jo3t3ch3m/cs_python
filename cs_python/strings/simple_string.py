# Python 2.7

# this is a simple program to show a basic string

prompt = "Please type in your first name: "
#print(prompt)

# What's happening above:
# first we create a variable called prompt
# prompt is just a way of telling the user exactly what information you want from them.

# The value of that variable is a string
# In Python, a string is enclosed with a pair of single or double quotes.
# Python interprets this as a string, a collection of letters, symbols, or numbers.

# Finally, we use the print() function to return the prompt

# When you run it, the computer 'prompts' the user for their name. However,
# The user cannot actually type in their name. Let's fix this.

# We'll create a new variable called first_name
first_name = raw_input(prompt)

# Now, we'll introduce how Python takes input from the user;
# the raw_input() function

# Then we'll pass the value of the variable prompt inside of the raw_input function call
# Lastly, we'll have whatver the user typed in and a little greeting from the computer, returned on our screen

print("Hello " + first_name + "!")

# In the last line, we added a little greeting using (+) operator
