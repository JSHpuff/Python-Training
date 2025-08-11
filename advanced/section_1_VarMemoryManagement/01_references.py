# To find the memory address of an object referenced by a variable, 
# you pass the variable to the built-in id() function.
counter = 100

print(counter)
print(id(counter))
print(hex(id(counter)))

# id of counter count to 2
max = counter

# make new id
max = 999

# original counter id count to 0
counter = 1