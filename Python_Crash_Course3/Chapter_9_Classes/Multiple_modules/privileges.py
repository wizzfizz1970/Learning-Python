# privileges.py
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
        print(f"\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
