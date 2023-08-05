"""Defines a class which represent an ice crean stand"""

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Defines an Ice cream stand while inheriting from a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialises an ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Chocolate', 'Vanilla', 'Mint', 'Strawberry', 'Banana']
    
    def display_flavours(self):
        """Lists out the flavours of ice cream"""
        for flavour in self.flavours:
            print(flavour)
