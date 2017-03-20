# Python 2.7

# Modifying an Attribute's Value Through a Method

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

    def  update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('buick', 'skylark', 1966)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(100000) # calling the new method
my_new_car.read_odometer()

