'''7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches'''


# List of sandwich orders
sandwich_orders = ["tuna sandwich", "chicken sandwich", "veggie sandwich", "ham sandwich", "egg salad sandwich"]

# Empty list to store finished sandwiches
finished_sandwiches = []

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



