# Defines a class Restaurant

class Restaurant:
    """Defines a restautant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.name} is a restautant that serves {self.cuisine} food")

    def open_restaurant(self):
        """Displays an open for business message"""
        print(f"{self.name} is open!")
    
    def closed_restaurant(self):
        """Displays a closed for business message"""
        print(f"{self.name} is closed")
