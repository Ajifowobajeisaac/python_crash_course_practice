# Defines a class Restaurant

class Restaurant:
    """Defines a restautant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.name} is a restautant that serves {self.cuisine} food")

    def open_restaurant(self):
        """Displays an open for business message"""
        print(f"{self.name} is open!")
    
    def closed_restaurant(self):
        """Displays a closed for business message"""
        print(f"{self.name} is closed")

    def set_number_served(self, served):
        """Sets the number of customers served"""
        self.number_served = served

    def increment_number_served(self, increment):
        """Increments the number of customers served"""
        self.number_served = self.number_served + increment
