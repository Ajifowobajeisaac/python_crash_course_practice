"""Function that prints a book title"""
# Parameter - book title



def book(title):
    """Takes a book title and prints a statement"""
    print(f"\nMy favorite book is {title}\n")


prompt = "\nWhat is the name of your favorited book?\n"

title_jake = input(prompt)

book(title_jake)
