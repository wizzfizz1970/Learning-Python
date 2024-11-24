'''9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.'''

class User:
    # A class to represent a user
    def __init__(self, first_name, last_name, password, employee_number):
        # Initialize the user attributes
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.employee_number = employee_number

    def describe_user(self):
        # Print a description of the user
        print("\nDetails of user:")
        print(f" - Employee Number: {self.employee_number} Name: {self.first_name} {self.last_name}")
        print(f" - Password: {self.password}")

    def greet_user(self):
        """Print a personalized message for the user."""
        print(f"Good morning, {self.first_name} {self.last_name}! Hope you have a great day.")


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "can add post", 
                "can delete post", 
                "can ban user", 
                "can promote user", 
                "can view all posts"
            ]
        self.privileges = privileges

    def show_privileges(self):
        """List the administrator’s privileges."""
        print(f"\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")


# Admin class inheriting from User
class Admin(User):
    def __init__(self, first_name, last_name, password, employee_number):
        # Initialize the parent User class
        super().__init__(first_name, last_name, password, employee_number)
        # Initialize a Privileges instance as an attribute
        self.privileges = Privileges()

# Create an instance of Admin
admin_user = Admin("lisa", "smith", "securepassword", "800")

# Call the methods for the admin user
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()
