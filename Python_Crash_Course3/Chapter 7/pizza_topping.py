'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''


age = input("Please enter your current age ? ")

age = int(age)

while age > 0 :
    if age < 3:
        print("Your toddler ticket is free")

    elif age <= 12:
        print("Your childs ticket is $10")

    else:

        print(" your adult ticket is $15.00 ")
        



