class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 2)
    
x = SquareNumber(3)
print(x)