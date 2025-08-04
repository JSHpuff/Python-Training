import os

try:
    os.rename('readme.txt', 'notes.txt')

except FileNotFoundError as e:
    print(e)

except FileExistsError as e:
    print(e)