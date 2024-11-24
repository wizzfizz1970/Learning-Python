'''8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *'''

# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that have been printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)
# print_models.py

# Import the functions from the printing_functions module
import printing_functions

# Lists of unprinted and completed models
unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

# Use the imported functions to handle the printing and display
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)


