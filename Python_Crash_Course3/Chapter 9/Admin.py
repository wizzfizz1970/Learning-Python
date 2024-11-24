'''An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
 Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.'''

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


# Admin class inheriting from User
class Admin(User):
    def __init__(self, first_name, last_name, password, employee_number):
        # Initialize the parent User class
        super().__init__(first_name, last_name, password, employee_number)
        # Additional attribute for privileges
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can promote user", 
            "can view all posts"
        ]

    def show_privileges(self):
        """List the administrator’s privileges."""
        print(f"\nPrivileges of {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f" - {privilege}")


# Create an instance of Admin
admin_user = Admin("lisa", "smith", "securepassword", "800")

# Call the methods for the admin user
admin_user.describe_user()
admin_user.greet_user()
admin_user.show_privileges()
