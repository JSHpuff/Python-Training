class Person:
    def __new__(cls, first_name, last_name):
        # Create a new object
        obj = super().__new__(cls)
        
        # Initialize Attributes
        obj.firstname = first_name
        obj.lastname = last_name
        
        # Inject New Attribute
        obj.full_name = f'{first_name} {last_name}'

        return obj
    
person = Person('John', 'Doe')
print(person.full_name)
print(person.__dict__)