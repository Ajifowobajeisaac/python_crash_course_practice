# Defines a User class

class User:
    """Defines a user"""
    def __init__(self, first_name, last_name, age, occupation, gender, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.gender = gender
        self.hobby = hobby


    def describe_user(self):
        """Describes the user listing key information"""
        print(f"{self.first_name} {self.last_name} is a {self.age} year old"
        f" {self.occupation}")
        if self.gender == 'Male':
            print(f"He loves {self.hobby}")
        elif self.gender == 'Female':
            print(f"She loves {self.hobby}")

    def greet(self):
        """Prints a greeting"""
        print(f"Hello {self.first_name}, How are you doing today?")
