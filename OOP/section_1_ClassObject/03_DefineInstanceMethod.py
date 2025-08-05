class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi, it's {self.name}."

person = Person('Jhon', 25)
print(person.greet())