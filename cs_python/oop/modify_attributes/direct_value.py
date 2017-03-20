# Python 2.7

# Directly Modifying an Attribute's Value

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

my_new_car.odometer_reading = 100 # directly modify the attribute
my_new_car.read_odometer()

