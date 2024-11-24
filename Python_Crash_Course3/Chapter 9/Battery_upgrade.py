'''9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range'''

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class, then initialize the electric car's specific attributes."""
        super().__init__(make, model, year)
        self.battery = Battery()  # Creating an instance of Battery class for ElectricCar

    def get_range(self):
        """Return the car's range based on the battery size."""
        return self.battery.get_range()


class Battery:
    """A class to model the battery of an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def get_range(self):
        """Return the car's range based on the battery size."""
        if self.battery_size == 70:
            return 240  # Default range for 70 kWh battery
        elif self.battery_size == 85:
            return 270  # Range for 85 kWh battery

    def upgrade_battery(self):
        """Upgrade the battery to 85 kWh if it isn't already."""
        if self.battery_size < 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kWh.")
        else:
            print("Battery is already at 85 kWh.")


# Create an electric car instance with a default battery size (70 kWh)
my_car = ElectricCar("Tesla", "Model S", 2024)

# Display the car's descriptive name and range before upgrading the battery
print(my_car.get_descriptive_name())
print(f"Range before upgrade: {my_car.get_range()} miles")

# Upgrade the battery and display the range again
my_car.battery.upgrade_battery()
print(f"Range after upgrade: {my_car.get_range()} miles")

