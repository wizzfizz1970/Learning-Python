"""8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list"""

def show_magicians(magicians):
    """Prints the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

# List of magician names
magicians = ["houdini", "david copperfield", "penn", "teller"]

# Call the function with the list
show_magicians(magicians)





