# Python 2.7

# Avoid Infinite Loops

# Every loop needs a way to stop running so it won't continue to run forever.
# For example, this counting loop should count from 1 to 5:

x = 1
while x <= 5:
    print(x)
    #x +=1
# However, if the last line isn't present, the loop will run forever!
# Comment the last line (x += 1) to see this in action.

# If your program is stuck in an infinite loop, you can always press CTRL-C,
# or just close the terminal window that is displaying the output.

# To avoid writing infinite loops, test every while loop and make sure the loop
# stops running when you expect it to.
