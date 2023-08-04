"""Show List Slices usages and operations"""

spices = ["Basil", "Parsley", "Roesmary", "Thyme", "Cummin", "Paprika", "Ginger"
          , "Tumeric", "Oregano","Sage", "Chili powder", "Coriander"]


spices_link = spices
# print(spices)
# print()
# print(spices_link)

removed_spice = spices.pop(-4)
# print(f"\n{removed_spice} has been removed\n")
# print(spices)
# print()
# print(spices_link)

#The above code shows that assigning the list variable to an empty variable
# link them rather than creating a copy. It just add an extra variable ponting
# at the same data

# Below is how to copy a list properly
spices_copy = spices[:]
# print()
# print(spices)
# print()
# print(spices_copy)

removed_spice = spices.pop(-4)
# print(f"\n{removed_spice} has been removed\n")
# print()
# print(spices)
# print()
# print(spices_copy)




# The code below shows a search through a list

print(spices, '\n')


if 'Ginger' in spices:
    print("True")
else:
    print("False")

if 'Tumeric' not in spices:
    print("True")
else:
    print("False")


# Tests to confirm if list was copied or linked
print()
print(spices == spices)
print(spices == spices_link)
print(spices == spices_copy)
