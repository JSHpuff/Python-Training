def a(func):
    print('makeup...')
    return func

def b():
    print('go!!!')

b = a(b)
b()