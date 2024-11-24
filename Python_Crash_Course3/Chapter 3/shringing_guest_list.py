"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program."""


uest = ['liam','chelsea','lillie']

message = 'I would like to invte you to dinner '

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

message2 = '\nSorry you cannot make it '

print(guest[0].title() + message2)

guest[0] = 'rebecca'
print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

print("\ngood nnews i found a bigger table\n")

guest.insert(0, 'sue')
guest.insert(2, 'eric')
guest.append('kevin')

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())
print(message + guest[3].title())
print(message + guest[4].title())
print(message + guest[5].title())

print("\nTable is to small ownly two people can come.\n")

print(message2 + guest.pop())
print(message2 + guest.pop())
print(message2 + guest.pop())
print(message2 + guest.pop())

message3 = "\nYou are still invited "
print(message3 + guest[0].title())
print(message3 + guest[1].title())

del guest[0]
del guest[0]

print(guest)
