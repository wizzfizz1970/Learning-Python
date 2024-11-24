'''9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
    Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
    Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.'''

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

# Create an instance of the Restaurant class
restaurant = Restaurant("Tasty Treats", "Italian")

# Print the default number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Update and print the number served
restaurant.set_number_served(25)
print(f"Number of customers served: {restaurant.number_served}")

# Increment the number served and print it again
restaurant.increment_number_served(30)
print(f"Number of customers served: {restaurant.number_served}")
