"""Demonstrates the ability of dictionaries to be nested within dictionaries"""

# Pseudocode
# A record of country information.
# Key - Country (string)
# Value - country_info (dictionary)
    # - keys -
        # continent (string)
        # language (string)
        # currency (string)
        # population (integer)
        # area (integer)

country = {
    'uk' : {
        'continent' : 'europe',
        'language' : 'english',
        'currency' : 'pound',
        'population' : 67_000_000,
        'area' : 250_000,
    },
    'usa' : {
        'continent' : 'america',
        'language' : 'english',
        'currency' : 'dollar',
        'population' : 318_000_000,
        'area' : 10_000_000,
    },
    'china' : {
        'continent' : 'asia',
        'language' : 'chinese',
        'currency' : 'yuan',
        'population' : 1_500_000_000,
        'area' : 9_500_000,
    },'russia' : {
        'continent' : 'europe',
        'language' : 'russian',
        'currency' : 'ruble',
        'population' : 144_000_000,
        'area' : 17_000_000,
    },
}


for place, facts in country.items():
    # print(f'{place}:')
    for key, value in facts.items():
        # print(f'{key}: {value}')
        continent = facts['continent']
        language = facts['language']
        currency = facts['currency']
        population = facts['population']
        area = facts['area']
    print()

    print(f'{place} is located in {continent} and spans over an area of {area}. '
          f'Its has a population of {population}. Residents speak {language} '
          f'and spend the {currency}.')


test = country.get('uk', "nada_____")
print('\n', test)
