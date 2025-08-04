def inc(numbers, value):
    numbers[0] += value
    return numbers[0]

numbers = [0]

s = f'{inc(numbers, 1)}, {inc(numbers, 2)}'
print(s)