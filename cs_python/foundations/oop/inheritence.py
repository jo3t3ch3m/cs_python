# Python 2.7

# Instead of starting from square one when writing a class,
# you can use inheritance if the new class is a specialized version
# of another you wrote.

# When one class inherits from another, it automatically takes on all the
# attributes and methods of the original class.

# The original class is called the "parent" class
# and the new class is called the "child" class.

# Though the child class inherits all the attributes and methods from its
# parent class, it can also define new attributes and methods of its own.

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " +str(self.odometer_reading) + " miles on it.")

    def  update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Starting child class:
class ElectricCar(Car):
    """Represent aspects of a car, specifically electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


