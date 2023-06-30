# A series of boolean tests 

# Testing equality/inequality with strings
print("Testing equality/inequality with strings:")
print("Private" == "Secret") 
print()

# Testing with lower() method
print("Testing with lower() method:")
print("Captain".lower() == "captain")
print("Captain".lower() == "captain".lower())
print("Captain".lower() == "CaPTaiN")
print("Captain".lower() == "CaPTaiN".lower())
print()

# Testing numerical equivalance
print("Testing numerical equivalance")
print(1 > 2)
print(1 >= 2)
print(1 <= 2)
print(1 == 2)
print()

# Tests with the "and" and "or" keywords
# Also tests the presence or absence of an item in a list
print("Tests with the 'and' and 'or' keywords")
print("Also tests the presence or absence of an item in a list")
even_numbers = [even_number for even_number in range(0, 90, 2)]
print(4 in even_numbers)
print(4 and 8 in even_numbers)
print(4 and 9 in even_numbers)
print(4 or 9 in even_numbers)
print()

