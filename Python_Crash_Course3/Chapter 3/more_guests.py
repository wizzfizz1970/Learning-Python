"""3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

guest = ['liam','chelsea','lillie']

message = 'I would like to invte you to dinner '

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

print(guest[0].title() +" can not make it")

guest[0] = 'rebecca'
print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

print("good nnews i found a bigger table")

guest.insert(0, 'sue')
guest.insert(2, 'eric')
guest.append('kevin')

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())
print(message + guest[3].title())
print(message + guest[4].title())
print(message + guest[5].title())