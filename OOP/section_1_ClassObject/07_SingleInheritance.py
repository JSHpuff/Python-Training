class Person:

    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1
    
    def greet(self):
        return f"Hi, it's {self.name}."
    
    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)

class Employee(Person):
    
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."

employee = Employee('Jhon', 25, 'Python Developer')
print(employee.greet())