"""Demonstrates dictionary functionalities"""

# A dictionary of people and their food allergens

people = {
    'anita' : [
        'fish',
        'eggs',
        'meat'
    ],
    'kyle' : [
        'gluten',
        'dairy',
        'meat'
    ],
    'toma' : [
        'nuts',
        'peanuts',
        'mustard'
    ],
    'kyle' : [
        'soya',
        'sulphates',
        'lupin'
    ],
    'samanta' : [
        'fish',
        'eggs',
        'meat'
    ],
    'lee' : [
        'gluten',
        'celery',
        'milk'
    ],
    'jide' : [
        'crustacean',
        'molluscs',
        'mustard'
    ],
    'kyle' : [
        'soya',
        'crustacean',
        'celery'
    ]
    
}


[print(person.title()) for person in people.keys()]

# print  'name' is allergic to 'allergies'

print()
[print(f'{name} is allergic to {allergen}') for name, allergens in people.items() 
 for allergen in allergens ]

print()
for name, allergens in people.items():
    print(f'{name} is allergic to:\t')   
    for allergen in allergens:
        print(f'\t{allergen}')
    print()
