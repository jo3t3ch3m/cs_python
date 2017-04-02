# CREATING AND USING A CLASS

# You can model almost anything using classes. Let's start by writing a simple
# class, Computer, that represents a modern computer --not one computer in particular, but any modern computer.
# What do we know about most modern computers?
# They have a name and can store memory.
# and many computers can take input and display input.
# The two pieces of information (name and memory capacity)
# and the two behaviors (input and output) can go in the class Computer,
# because they are common to most computers (modern ones).

# This class will tell Python how to make an object representing a computer.
# After this class is written, we'll use it to make individual instances,
# each of whcih represents one specific computer.

# CREATING THE COMPUTER CLASS
# Each instance created from the Computer class will store a name and a memory capacity,
# and we'll give each computer the ability to take_input() and display_input():

class Computer():
    """A simple attempt to model a modern computer."""

    def __init__(self, name, memory):
        """Initialize name and age attributes."""
        self.name = name
        self.memory = memory

    def take_input(self):
        """Simulate a computer accepting input in response to a given command."""
        print(self.name.title() + " is now accepting input.")

    def display_output(self):
        """Simulate displaying information in response to input."""
        print(self.name.title() + " displayed output!")

# THE ___init__() METHOD

# A method is a function that is part of a class.
# Methods are much the same as functions. The difference (for now) is the
# the way we call methods. The __init__() is a special method that Python runs
# automatically whenever we create a new instance based on the Computer class.

# We define the __init__() method to have three paremeters: self, name, and memory.
# The self parameter is required in the method definition, and it must come
# first before the other paremeters. The reason for this, is so when Python
# calls this __init__() method later (to create an isntance of a computer),
# the method call will automatically pass the self argument.

# Every method call associated with a class automatically passes self

# MAKING AN INSTANCE FROM A CLASS

# Think of a class as a set of instructions for how to make an instance.
# The class Computer is a set of isntructions that tells Python how to make
# individual instances representing specific computers.

# Let's make an instance representing a specific computer:

my_computer = Computer('TRS-80', 16)

print("My computer's name is " + my_computer.name.upper() + ".")
print("My computer has " + str(my_computer.memory) + " kilobytes of volatile memory.")
my_computer.take_input()
my_computer.display_output()



