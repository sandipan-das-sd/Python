class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class TyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortunar(Car):  # Inherit from Car class
    def __init__(self, car_type):
        super().__init__()
        self.car_type = car_type

car1 = Fortunar("diesel")
car1.start()  # Now this will work
