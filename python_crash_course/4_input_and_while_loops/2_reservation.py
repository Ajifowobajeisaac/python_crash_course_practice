"""Demonstrates how to get user input"""

# A progams that acts the user 'how many guests are in the diner group'

prompt = "To provide the right seating for you, we need to know the size of your "
prompt += "group.\nWhat is the number of your diner group?: "

group = input(prompt)
group = int(group)

if group < 2:
    print("Dining alone? We have the perfect seat with the best view")
elif group == 2:
    print("Enjou our special couple table for your intimate night")
elif group > 7:
    print("You'll need to nnake a special table reservation for the night")
else:
    print("Great! There's an available table for you") 
