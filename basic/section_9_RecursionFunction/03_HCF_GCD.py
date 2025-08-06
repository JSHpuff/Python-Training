# highest common factor, hcf
# greatest common divisor, gcd

def f(a, b):
    if a % b == 0:
        return b
    else:
        return f(b, a % b)

print(f(456, 48))