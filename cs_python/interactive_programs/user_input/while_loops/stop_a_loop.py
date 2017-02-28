# Python 2.7

# consider the greeter program:
# Remember to write clear prompts!

prompt = ("\nPlease enter your name:")
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = raw_input(prompt)
    print(message)

# This program works well, except that it prints the word 'quit' as if it
# were an actual message.
# How can we fix this?

#############################
#############################

message = ""
while message != 'quit':
    message = raw_input(prompt)

    if message != 'quit':
        print(message)
