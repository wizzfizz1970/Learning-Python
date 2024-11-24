'''7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''



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
