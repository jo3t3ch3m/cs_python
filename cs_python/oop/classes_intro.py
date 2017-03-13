# Python 2.7

# CREATING AND USING A CLASS

class Dog():
    """a simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

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

your_dog('teddy', 3)

