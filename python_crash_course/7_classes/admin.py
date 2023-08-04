"""Defines a class Admin which inherites from User class. Admin has special
priviledges"""

from user import User


class Admin(User):
    """An admin user class with extra priviledges"""
    def __init__(self, first_name, last_name, age, occupation, gender, hobby):
        """Initializes an admin user class and add priviledges attribute"""
        super().__init__(first_name, last_name, age, occupation, gender, hobby)
        self.priviledges = Priviledges()

class Priviledges:
    """A class that defines user priviledges for the class User"""
    def __init__(self):
        """Initializes priviledges"""
        self.priviledges = [
            "Can add post",
            "Can delete post",
            "Can ban users",
            "Can suspend users",
        ]


    def show_priviledges(self):
        """Display the priviledges available to the admin"""
        print("Admin:")
        for priviledge in self.priviledges:
            print(f"\t{priviledge}")
        print()
