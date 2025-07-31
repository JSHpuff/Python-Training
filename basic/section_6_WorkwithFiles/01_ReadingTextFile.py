# 1.
with open('test.txt') as f:
    contents = f.read()
    print(contents)

# 2.
with open('test.txt') as f:
    [print(line) for line in f.readlines()]

# 3.
with open('test.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())