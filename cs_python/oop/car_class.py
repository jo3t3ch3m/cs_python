# Python 2.7

# Again, OOP allows you to represent many real-world situations.

# Once you've created a class, you'll spend a lot of time working with
# different instances of that class. Recall the things.py program where
# we described a dog (in general). To describe a specific dog, we created
# instances from the class Dog.

# One of the first things we did was changing the attributes associated with
# the class with a specific instance. We either directly modified the attributes
# or we wrote new methods that updated the attributes in specific ways.

# Let's write a class representing a car. The class will store information about the
# kind of car we're working with, and it will have a method that summarizes the info.

class Car():
    """attempting to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # new odometer instance
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a foramtted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    # adding odometer reading
    def read_odometer(self):
        """returning a statement showing the car's mileage."""
        print("This car has " +str(self.odometer_reading) + " miles on it.")


my_new_car = Car('buick', 'skylark', 1966)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Since this car probably won't have 0 miles driven.
# There are three ways we can do this: directly change the value through an instance,
# or set the value through a method, or increment the value through a method.
