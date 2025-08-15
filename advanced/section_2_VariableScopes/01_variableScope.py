counter = 10

def reset():
    counter = 0
    print(counter) # 0

reset()
print(counter)  # 10

def reset_global():
    global counter
    counter = 0
    print(counter) # 0

reset()
print(counter) # 0