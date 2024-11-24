'''9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.'''

class User:
    # A class to represent a user

    def __init__(self, first_name, last_name, password, employee_number):

        # Initialize the user attributes.

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.employee_number = employee_number

    def describe_user(self):   
        # Print a description of the user.
        print("\nDetails of user:")
        print(f" - Employee Number: {self.employee_number} Name: {self.first_name} {self.last_name}")
        print(f" - Password: {self.password}")

    def greet_user(self):
        """Print a personalized message for the user."""
        print(f"Good morning, {self.first_name} {self.last_name}! Hope you have a great day.")

# Create instances of the User class
user1 = User("kevin", "brown", "cat", "700")
user2 = User("rebecca", "jones", "dog", "701")
user3 = User("liam", "harper", "mouse", "702")

# Call the methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()




        

