import random 

# List choose 2 elements
print(random.choices([1, 2, 3, 4, 5], k=2))

# Tuple choose 3 elements
print(random.choices((1, 2, 3, 4, 5), k=3))

# String choose 4 elements
print(random.choices('12345', k=4))