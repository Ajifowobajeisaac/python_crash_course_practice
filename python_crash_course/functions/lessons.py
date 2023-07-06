# Demonstrates the use of functions


def lessons():
    """Displays some programming tip I've learnt"""
    print("""\n1. When nameing a list, enusure it has a plural name so the lits
        items can be singular\n2. The variable names should be thoughtful to ensure 
          readability of code\n 3. It's better to for the code to be be easy to
          read than easy to write (if it's a choice between the two)""")
    


tips_prompt = "\nWould you like to get some programming tips? type Y or N:\n"

tips = input(tips_prompt)


if tips == 'y':
    lessons()
