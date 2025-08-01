# 1.
import os.path
file_exists = os.path.exists('readme.txt')
print(file_exists)

# 2. 
from os.path import exists as file_exist
file_exist('readme.txt')

# 3.
from pathlib import Path
path_to_file = 'readme.txt'
path = Path(path_to_file)
if path.is_file():
    print(f'The file {path_to_file} exists')
else:
    print(f'The file {path_to_file} does not exist')