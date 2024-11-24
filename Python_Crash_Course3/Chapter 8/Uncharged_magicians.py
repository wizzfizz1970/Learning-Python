'''8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.'''

def show_magicians(magicians):
    """Prints the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Returns a new list of magicians with 'the Great' added to each name."""
    great_magicians = [f"The Great {magician}" for magician in magicians]
    return great_magicians

# Original list of magician names
magicians = ["Houdini", "David Copperfield", "Penn", "Teller"]

# Create a new list with 'the Great' added
great_magicians = make_great(magicians)

# Show the original list
print("Original Magicians:")
show_magicians(magicians)

print("\nGreat Magicians:")
# Show the new list
show_magicians(great_magicians)
