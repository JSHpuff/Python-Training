lines = ['Readme', 'How to write text files in Python']

# 1.
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# 2.
with open('readme.txt', 'w') as f:
    f.writelines(lines)

# 3.
with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))