'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.'''

# Import the Restaurant class from the restaurant module
from restaurant import Restaurant

# Create instances of the Restaurant class
restaurant1 = Restaurant("The Gourmet Spot", "Italian")
restaurant2 = Restaurant("Spicy Corner", "Indian")
restaurant3 = Restaurant("Ocean Delights", "Seafood")

# Call the methods for each restaurant instance
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()
