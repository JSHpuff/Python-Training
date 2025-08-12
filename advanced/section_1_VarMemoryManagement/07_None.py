# 1. 
print(type(None))

# 2. 
print(None == None) # True
print(None is None) # True

# 3.
class Apple:
    def __eq__(self, other):
        return True

apple = Apple()
print(apple == None)    # True

# 4. 
def append(color, colors=None):
    if colors is None:
        colors = []
    colors.append(color)
    return colors

hsl = append('hue')
print(hsl)
rgb = append('red')
print(rgb)