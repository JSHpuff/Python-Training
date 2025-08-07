import math

print(math.isclose(10, 10.4, abs_tol=0.5)) # True 0.4 < 0.5
print(math.isclose(10, 10.6, abs_tol=0.5)) # False 0.6 > 0.5