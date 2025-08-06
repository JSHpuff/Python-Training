class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age
    
    def __hash__(self):
        return hash(self.age)
    