# Demonstrates the ability of functions to take lists as inputs
# Other data strcutures can be taken as input also

quotes = [ 
    "The only true wisdom is in knowing you know nothing. - Socrates",
    "The greater the obstacle, the more glory in overcoming it. - Molière",
    "No pressure, no diamonds. — Thomas Carlyle",
    "Challenges are what make life interesting and overcoming them is what makes"
    "life meaningful. - Joshua J. Marine",
    "We don't grow when things are easy; we grow when we face challenges."
    "- Joyce Meyer",
    "When we are no longer able to change a situation, we are challenged to"
    "change ourselves. - Viktor E. Frankl",
    "The measure of intelligence is the ability to change. - Albert Einstein",
    "Truth is ever to be found in simplicity, and not in the multiplicity and"
    "confusion of things. - Isaac Newton",
    "Peace comes from within. Do not seek it without. - Buddha",
]


def show_qoutes(quotes):
    """Prints each quote from a list of quotes"""
    for quote in quotes:
        print(f'\n{quote}')
        print(len(quote))

show_qoutes(quotes)

def short_quotes(quotes):
    """Takes a lists of quotes and returns a new list of short quotes"""
    new_list = []
    while quotes:
        quote = quotes.pop()
        if len(quote) < 70:
            new_list.append(quote)

    return new_list

# The function is called with a slice to create a copy to avoid destroying the
# original list
new_s_quotes = short_quotes(quotes[:])

print('------------------------')
show_qoutes(new_s_quotes)
print('------------------------')
show_qoutes(quotes)

