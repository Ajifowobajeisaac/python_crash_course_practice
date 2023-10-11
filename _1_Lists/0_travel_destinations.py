"""A demonstrations of list operations"""

place = ["Ibiza", "Mykonos", "Paris", "Bali"]

print(place)
print(sorted(place))

print(f"\n", place)
print(sorted(place, reverse = True))

print(f"\n", place)
place.reverse()
print(place)

print(f"\n", place)
place.reverse()
print(place)

print(f"\n", place)
place.sort()
print(place)

print(f"\n", place)
place.sort(reverse=True)
print(place)


print(len(place))
