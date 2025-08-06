def a(func):
    print('makeup...')
    return func

@a
def b():
    print('go!!!')

b()