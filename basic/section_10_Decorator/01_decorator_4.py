def a(func):
    def c(m):
        print('makeup...')
        return func(m)
    return c

@a
def b(msg):
    print(msg)

b('go!!!')