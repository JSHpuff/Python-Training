colors = ['red', 'green', 'blue']

try:
    print(colors[3])
except LookupError as e:
    print(e.__class__, '-', e)

print('Continue to run')