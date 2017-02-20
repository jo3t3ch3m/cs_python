# Python 2.7


# again, consider a imple parrot program...
prompt = ("\nTell me something, and I will repeat it back to you:")
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = raw_input(prompt)

    if message != 'quit':
        print(message)
# This program performs its task while a given condition is true.
# But, what about a more compplicated programs in which many different events
# could cause the program to stop running?

# Think of a game.
# Usually, several differentt events can end the game.
# i.e. when time runs out, when the player dies, when an enemy reaches a certain point, etc.
# If these examples occur, it can make the program end.

# If many possible events might occur to stop the program, just trying to test
# all these conditions in one while statement can become complicated and difficult!
###################
# Enter... FLAG
# For a program that should run only as long as many conditions are true, you
# can define one variable that determiens whether or not the entire the program is active.
# This variable, called a flag, acts as a signal to the program.

# We can run our programs so they run while the flag is set to True
# and stop running when any of several events sets the value of the flag to False

# so... SO, our overall while statement needs to check only one condition:
# whether or not the flag is currently True.
# This way, all our other tests can be neatly organized in the rest of the program.
