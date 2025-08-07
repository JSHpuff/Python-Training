class Person:
    def __init__(self, name):
        self.name = name

person = Person('John')

# Equivalent
person = object.__new__(Person, 'John')
person.__init__('John')