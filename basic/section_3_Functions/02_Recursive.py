def count_down(start):
    ''' Count down from a number '''
    print(start)
    # Call the count_down if the next number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)

count_down(3)

def sum(n):
    return n + sum(n-1) if n > 0 else 0

result = sum(100)
print(result)