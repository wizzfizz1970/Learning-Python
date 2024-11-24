# admin.py
from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, password, employee_number):
        super().__init__(first_name, last_name, password, employee_number)
        self.privileges = Privileges()

# Create an instance of Admin
admin_user = Admin("lisa", "smith", "securepassword", "800")

# Call the methods for the admin user
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()
