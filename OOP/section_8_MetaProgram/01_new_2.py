class Person:
    def __new__(cls, name):
        print(f'Creating a new {cls.__name__} object...')
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, name):
        print(f'Initializing the person object...')
        self.name = name

person = Person('John')