"""Contflow techniques"""

# Checks if usernames are unique
print("checks if usernames are unique")

current_users = ["Ron", "James", "Kay", "Riri", "Silva"]
new_users = ["Mark", "Silva", "Dave", "Tony", "Riri"]

if current_users:
    if new_users:
        for new_user in new_users:
            if new_user in current_users:
                print("Sorry, this name has already been used")
            else:
                print("This username is available")
 