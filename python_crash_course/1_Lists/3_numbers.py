"""Shows the range function and list comprehensions"""

numbers = [number for number in range(1000001)]
# [print(number) for number in numbers]
print(min(numbers))
print(max(numbers))

print()
[print(number) for number in range(1, 20, 2)]
print()
# [print(number*3) for number in range(3, 30)]
print()
[print(number**3) for number in range(1, 10)]
print()
print(numbers[0:4])
