def count_down(start):
    ''' Count down from a number '''
    print(start)
    # Call the count_down if the next number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)

count_down(3)