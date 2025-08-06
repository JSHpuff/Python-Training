def a(func):
    def c(*args, **kwargs):
        print(args)
        print(kwargs)
        print('ok...')
        return func(*args, **kwargs)
    return c

@a
def b(*arg, **kwargs):
    print('go!!!!')

b([123, 456], x=1, y=2, z=3)
