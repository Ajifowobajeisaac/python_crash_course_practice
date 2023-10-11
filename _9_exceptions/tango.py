"""Random shit"""

words = ['amiable', 'Usurious', 'Hark', 'Ubiquitous']

try:
    word_of_the_day = words[6]
    print(word_of_the_day) 
except IndexError:
    print("That doesn't exist yet :-)")
