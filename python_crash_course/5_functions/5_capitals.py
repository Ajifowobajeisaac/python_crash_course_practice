"""This program displays arbitrary keyword arguments (kwargs)"""

def state_capital(**state_capitals):
    """Takes a varying numbe of state and capital pairs and prints them"""
    for s,c in state_capitals.items():
        print(f"The capital of {s} is {c}")


state_capital(India = 'delhi', Japan = 'Tokyo', England = 'London')


# We can make this programme more specific to a country
# A postitional argument will be used of the country and the kwargs will be for
# additional details which are unknown

def country_details(country, **details):
    """Creates a dictionary containing details of a country"""
    details['Country'] = country
    return details

japan = country_details('Japan', Capital = 'Tokyo', population = 125_700_000)

print()
[print(f"{k} = {v}") for k,v in japan.items()]
