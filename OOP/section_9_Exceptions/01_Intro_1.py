colors = ['red', 'green', 'blue']

try:
    print(colors[3])
except IndexError as e:
    print(e)

print('Continue to run')