def fn(*args, **kwargs):
    print(args)
    print(kwargs)

fn(1, 2, x=10, y=20)