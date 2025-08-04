import os

# 1.
filename = 'readme.txt'
if os.path.exists(filename):
    os.remove(filename)

# 2.
try:
    os.remove('readme.txt')
except FileNotFoundError as e:
    print(e)