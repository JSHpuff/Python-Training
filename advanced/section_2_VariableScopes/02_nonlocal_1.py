def outer():
    print('outer function')
    def inner():
        print('inner function')
    inner()

outer()

# outer function
# inner function