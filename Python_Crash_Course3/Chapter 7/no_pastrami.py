'''7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.'''


# List of sandwich orders
sandwich_orders = ["tuna sandwich", "chicken sandwich", "veggie sandwich", "pastrami","pastrami","pastrami"]

# Empty list to store finished sandwiches
finished_sandwiches = []

# no pastrami
print('Soorry there be no pastrami sandwich due to we run out')

# remove pastrami from list

sandwich_orders = [sandwich for sandwich in sandwich_orders if sandwich != "pastrami"]

# Process each sandwich order
while sandwich_orders:
    # Get the first sandwich order
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    
    # Add the made sandwich to the finished sandwiches list
    finished_sandwiches.append(current_sandwich)

# Print the list of all finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")