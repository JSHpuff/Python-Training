def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as ex:
        raise ValueError('b must not be zero') from ex
    
try:
    divide(10, 0)
except ValueError as ex:
    print('cause', ex.__cause__)
    print('exception', ex)