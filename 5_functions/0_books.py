"""A showcase of Functions and inputs (Paramenters and arguments)"""
# Parameters - book title, gente

# This function only defines one paramenter. so it takes only one argument
def book_title(title):
    """Takes a book title and prints a statement"""
    print(f"\nMy favorite book is {title}")


# This function takes two postional arguments
def book(title, genre):
    """Takes a book title and prints a statement"""
    print(f"\nMy favorite book is {title}, it is a {genre} book\n")
    


prompt_title = "\nWhat is the name of your favorited book?\n"
title = input(prompt_title)

prompt_genre = f'What genre is {title}?\n'
genre = input(prompt_genre)


# Two different ways to call this function. One takes user input while the other
# has arguments fed directly into the function call 
book(title, genre)
book('Finley Road', 'Drama')

# Argument Position matters with position arguments. If we switch up the positions
# we would get wierd results
book('Drama', 'Romeo and Juliet')
