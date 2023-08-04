"""This program tests methods from the user class"""

from user import User

todd = User("Todd", "Smith", 34, "Investment Banker", "Male", "Tennis")
sharon = User("Sharon", "Gilbert", 19, "Student", "Female", "reading novels")


todd.describe_user()
todd.greet()
print()
sharon.describe_user()
sharon.greet()
