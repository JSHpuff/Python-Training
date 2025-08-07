from pprint import pprint

class Human(type):
    def __new__(mcs, name, bases, class_dict):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        return class_
    
class Person(object, metaclass=Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age

pprint(Person.__dict__)