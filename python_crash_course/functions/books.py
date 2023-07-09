# Function that prints a book title
# Parameter - book title



def book(title, genre):
    """Takes a book title and prints a statement"""
    print(f"\nMy favorite book is {title}, it is a {genre} book\n")
    


prompt_title = "\nWhat is the name of your favorited book?\n"
title = input(prompt_title)

prompt_genre = f'What genre is {title}?\n'
genre = input(prompt_genre)

book(title, genre)


