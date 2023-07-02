# Exercise on inputs

# This program takes an input then verifies whether it's a multiple of 8.

prompt = "Type a number:"

number = input(prompt)
number = int(number)

if number % 8 == 0:
    print("Bingo! This number is a multiple of eight")
else:
    print("Oh, not what we're looking for. Try again or quit with 'q'")
    number = input(prompt)
    if number == 'q':
        print("Thank you for playing")
