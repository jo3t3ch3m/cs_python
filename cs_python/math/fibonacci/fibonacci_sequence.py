"""
A simple program to display the fibonacci sequence.

The user is asked for the amount of number they want to be displayed.
The program then performs the fibonacci sequence for the amount of numbers inputted.

The first two items in the sequence are 0 and 1. All other items are obtained by
adding the preceding two items. In other words, the nth item is the sum of
(n-1) and (n-2).
"""

howMany = int(raw_input("How many numbers should I create?"))
nums = [0,1,1]

print(0)
print(1)
print(1)

for i in range(2, howMany):
    nextFib = nums[-1] + nums[-2] # takes the last item, second-to-last item and adds them
    nums.append(nextFib)
    print(nextFib)
    # and repeats for however many times the user specified
