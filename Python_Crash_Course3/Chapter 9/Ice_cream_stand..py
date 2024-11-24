'''9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.'''

class Restaurant:
    """A class to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type, and number served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of 0
    
    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")
    
    def set_number_served(self, number):
        """Set the number of customers served to a specific value."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")
    
    def increment_number_served(self, increment):
        """Increment the number of customers served by a specific value."""
        if increment > 0:
            self.number_served += increment
        else:
            print("Increment value must be positive.")

class IceCreamStand(Restaurant):
    """A class to represent an ice cream stand, which is a type of restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize the ice cream stand with name, cuisine type, and list of flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors  # List of ice cream flavors
    
    def display_flavors(self):
        """Display the list of ice cream flavors available at the stand."""
        print(f"Available ice cream flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Cool Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint"])

# Call the methods
ice_cream_stand.describe_restaurant()  # Inherited from Restaurant
ice_cream_stand.open_restaurant()  # Inherited from Restaurant
ice_cream_stand.display_flavors()  # Method specific to IceCreamStand
