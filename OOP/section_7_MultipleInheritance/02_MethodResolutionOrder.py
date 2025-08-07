class Car:
    def start(self):
        print('Start the Car')
    def go(self):
        print('Going')

class Flyable:
    def start(self):
        print('Start the Flyable object')
    def fly(self):
        print('Flying')

class FlyingCar(Flyable, Car):
    def start(self):
        super().start()

if __name__ == "__main__":
    car = FlyingCar()
    car.start()
    print(FlyingCar.__mro__)