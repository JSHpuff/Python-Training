class Shape:
    pass

class Point2D(Shape):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    point = Point2D(10, 10)
    print(point.__slots__)
    print(point.__dict__)

    point.color = 'black'
    print(point.__dict__)