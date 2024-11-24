# user.py
class User:
    def __init__(self, first_name, last_name, password, employee_number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.employee_number = employee_number

    def describe_user(self):
        print("\nDetails of user:")
        print(f" - Employee Number: {self.employee_number} Name: {self.first_name} {self.last_name}")
        print(f" - Password: {self.password}")

    def greet_user(self):
        print(f"Good morning, {self.first_name} {self.last_name}! Hope you have a great day.")
