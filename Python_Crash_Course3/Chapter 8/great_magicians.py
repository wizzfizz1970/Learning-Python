'''8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.'''

def show_magicians(magicians):
    """Prints the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifies the list of magicians by adding 'the Great' to each name."""
    for i in range(len(magicians)):
        magicians[i] = f"The Great {magicians[i]}"

# List of magician names
magicians = ["Houdini", "David Copperfield", "Penn", "Teller"]

# Modify the list with make_great
make_great(magicians)

# Call the function to display the modified list
show_magicians(magicians)

