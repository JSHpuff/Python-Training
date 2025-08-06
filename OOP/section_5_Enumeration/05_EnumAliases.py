from enum import Enum
from pprint import pprint

class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREEN = 2
    BLUE = 3

pprint(Color.__members__)