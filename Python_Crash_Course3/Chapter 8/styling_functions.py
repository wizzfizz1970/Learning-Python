'''8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section'''

def make_sandwich(*items):
    """Summarize the sandwich being ordered."""
    print("\nThe sandwich will have the following ingredients:")
    for item in items:
        print(f"- {item.title()}")

# Calling the function with different number of arguments
make_sandwich('lettuce', 'tomato', 'turkey')
make_sandwich('cheese', 'ham')
make_sandwich('avocado', 'bacon', 'egg', 'spinach')