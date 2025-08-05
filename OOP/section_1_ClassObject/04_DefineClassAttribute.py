class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

p1 = Person('John', 25)
p2 = Person('Jane', 22)

print(Person.counter)