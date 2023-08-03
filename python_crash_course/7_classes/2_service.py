from restaurant import Restaurant

tamberma = Restaurant("Tamberma", "Indian")
print(tamberma.number_served)

tamberma.number_served = 12
print(tamberma.number_served)
print()
tamberma.set_number_served(30)
print(tamberma.number_served)
print()
tamberma.increment_number_served(8)
print(tamberma.number_served)
