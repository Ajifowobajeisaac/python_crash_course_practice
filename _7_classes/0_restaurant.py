"""This program tests methods from the restaurant class"""

from restaurant import Restaurant

ayos = Restaurant("Ayos", "Turkish")

print(ayos.name)
print(f"\n{ayos.cuisine}\n")

ayos.describe_restaurant()
ayos.open_restaurant()
ayos.closed_restaurant()


print("-----------")
enish = Restaurant("Enish", "Nigerian")
roasted_duck = Restaurant("Roasted Duck", "Chinesse")
uzimaki = Restaurant("Uzimaki London", "Japanesse")

enish.describe_restaurant()
roasted_duck.describe_restaurant()
uzimaki.describe_restaurant()
