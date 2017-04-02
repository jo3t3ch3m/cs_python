# Python 2.7

# CREATING AND USING A CLASS

# You can model model almost anything using classes.

# Let's start by defining classes from our first example.

class Things():
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    pass

class Mammals(Animals):
    pass




# Finally we'll define our class Dog

# This won't represent one dog in particular, but any dog.

# To represent one specific dog, we'll create an instance from the class Dog.

class Dog(Mammals):
    """a simple attempt to model a dog"""

    # Create an instance based on the class Dog.
    # This instance will have three parameters: self, name, age
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # Make accessible attributes or variables:
        self.name = name
        self.age = age

    # Defining the methods of the class Dog
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# Making an instance representing a specific dog

my_dog = Dog('koa', 2)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " years old.")

# CALLING METHODS
my_dog.sit()
my_dog.roll_over()

# CREATING MULTIPLE INSTANCES

your_dog = Dog('teddy', 3)

