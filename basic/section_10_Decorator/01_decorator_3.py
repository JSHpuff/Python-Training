def a1(func):
    print('1')
    return func

def a2(func):
    print('2')
    return func

def a3(func):
    print('3')
    return func

@a1
@a2
@a3
def b():
    print('go!!!')

b()