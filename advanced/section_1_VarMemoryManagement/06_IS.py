# 1. 
a = 100
b = a
result = a is b
print(result) # True

# 2. 
a = 100
b = 100
result = a is b
print(result) # True

# 3.
ranks = [1, 2, 3]
rates = [1, 2, 3]
result = ranks is rates
print(result) # False

# 4. is vs ==
a = 100
b = a
is_identical = a is b
is_equal = a == b
print(is_identical) # True
print(is_equal)     # True

# 5. is vs ==
ranks = [1, 2, 3]
rates = [1, 2, 3]
is_identical = ranks is rates
is_equal = ranks == rates
print(is_identical) # False
print(is_equal)     # True

# 6. is not
ranks = [1, 2, 3]
rates = [1, 2, 3]
result = ranks is not rates
print(result)   # True