class Cat: 
    """A model of the cat family"""
    _number_alive = 0

    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age
        Cat._number_alive += 14
        print(f'A new {self.__class__} is born')

    def __str__(self):
        return "Cat"

    def get_desc(self):
        print(f'my name is {self.name}, I am {self.age} years old and my colour is {self.colour}')

    def die(self):
        print(f'{self.name} has kicked the bucket')
        Cat._number_alive -= 1

    @classmethod    
    def get_populatation(cls):
        print(f'There are {Cat._number_alive} cats left')
        return Cat._number_alive

class Tiger(Cat):
    """A model of a tiger"""

    def __init__(self, name, colour, age):
        super().__init__(name, colour, age)
    
    def hunt(self):
        print(f'{self.name} has killed his prey')


lucky = Cat("lucky", 'white', 12)
lucky.get_desc()
Cat.get_populatation()
matty = Cat("matty", "blue", 10)
jimmy = Tiger("Jim", "red", 3)
brad = Tiger("bram", "lemon", 6)
stunner = Tiger("stunner", "black", 61)
Cat.get_populatation()
brad.get_desc()
jimmy.hunt()
lucky.die()
Cat.get_populatation()


