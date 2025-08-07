class Car:
    def go(self):
        print('Going')

class Flyable:
    def fly(self):
        print('Flying')

class FlyingCar(Flyable, Car):
    pass

if __name__ == "__main__":
    fc = FlyingCar()
    fc.go()
    fc.fly()