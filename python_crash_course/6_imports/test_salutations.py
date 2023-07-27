import random

salutations = ["Hello", "Hey", "Hi", "Hiya", "Howdy"]

emphatic_salutations = []
for greeting in salutations:
    emphatic_salutations.append(greeting + "!")
salutations.extend(emphatic_salutations)

def greet():
    """Print a salutation."""
    print(random.choice(salutations))

print("Test calling greet:", greet())

def part():
    """Print a valediction."""
    print("Live long and prosper")

print("Test calling part:", part())
