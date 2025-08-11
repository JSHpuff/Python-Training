import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

numbers = [1, 2, 3]
numbers_id = id(numbers)

print(ref_count(numbers_id))

ranks = numbers
print(ref_count(numbers_id))

ranks = None
print(ref_count(numbers_id))

numbers = None
print(ref_count(numbers_id))