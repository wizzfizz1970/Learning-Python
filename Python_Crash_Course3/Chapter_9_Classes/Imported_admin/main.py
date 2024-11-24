'''9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.'''

# main.py

# Importing the classes from user_privileges.py
from user_privileges import Admin

# Create an instance of Admin
admin_user = Admin("lisa", "smith", "securepassword", "800")

# Call the methods for the admin user
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()
