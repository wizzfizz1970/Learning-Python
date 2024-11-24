'''7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.'''


prompt = "\nThere are three exits numbered 1, 2 and 3 please enter one ?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    exit = input(prompt)
    if exit == 'quit':
        break
    exit = int(exit)

    if exit == 3:
        print("You used exit 3")
    elif exit == 2:
        print("You used exit 2")
    else:
        print("You used exit 1")
