'''9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''

class User:
    # A class to represent a user

    def __init__(self, first_name, last_name, password, employee_number):
        # Initialize the user attributes.
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.employee_number = employee_number
        self.login_attempts = 0  # New attribute to track login attempts

    def describe_user(self):   
        # Print a description of the user.
        print("\nDetails of user:")
        print(f" - Employee Number: {self.employee_number} Name: {self.first_name} {self.last_name}")
        print(f" - Password: {self.password}")
        print(f" - Login Attempts: {self.login_attempts}")

    def greet_user(self):
        """Print a personalized message for the user."""
        print(f"Good morning, {self.first_name} {self.last_name}! Hope you have a great day.")

    def increment_login_attempts(self):
        """Increase the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0

# Create an instance of the User class
user1 = User("kevin", "brown", "cat", "700")

# Increment login attempts several times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the login attempts to ensure it was incremented
print(f"\nLogin attempts after incrementing: {user1.login_attempts}")

# Reset the login attempts
user1.reset_login_attempts()

# Print the login attempts to ensure it was reset
print(f"Login attempts after resetting: {user1.login_attempts}")
