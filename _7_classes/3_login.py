""""This programs tests a method for incrementing a class attributes"""

from user import User

greg = User("Greg", "Farshaw", 29, "Carpenter", "Male", "Bird watching")

print(greg.login_attempts)
greg.increment_login_attempt()
greg.increment_login_attempt()
greg.increment_login_attempt()
greg.increment_login_attempt()
print(greg.login_attempts)
greg.reset_login_attempts()
print(greg.login_attempts)
