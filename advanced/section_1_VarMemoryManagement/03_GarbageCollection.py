# 在 Python 裡，垃圾回收（Garbage Collection, GC） 
# 就是自動釋放不再被程式使用的記憶體，讓你不用像 C 語言一樣手動 free()。

# 沒有循環引用 →    del 就夠了，因為計數會變 0。
# 有循環引用 →     還要靠 gc.collect() 來處理。

import gc
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True
    return False

class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')

class B:
    def __init__(self, a):
        self.a = a
        print(f'B: {hex(id(self))}, A: {hex(id(self.a))}')

# Disable the garbage collector
gc.disable()

a = A()
a_id = id(a)
b_id = id(a, b)

print(ref_count(a_id)) # 2
print(ref_count(b_id)) # 1

print(object_exists(a_id)) # True
print(object_exists(b_id)) # True

a = None

print(ref_count(a_id)) # 1
print(ref_count(b_id)) # 1

print(object_exists(a_id)) # True
print(object_exists(b_id)) # True

# Run the garbage collector
gc.collect()

# Check if object exists
print(object_exists(a_id)) # False
print(object_exists(b_id)) # False

# Reference count
print(ref_count(a_id)) # 0
print(ref_count(b_id)) # 0