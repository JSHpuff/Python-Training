from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(type(Color.RED))
print(isinstance(Color.RED, Color))
print(Color.RED.name)
print(Color.RED.value)
