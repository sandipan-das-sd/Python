'''
When one class (childderived) derives the properties & methods of another class(parent base)
'''
class Car:
    color="black"
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")
class TyotaCar(Car):
    def __init__(self,name) :
        self.name=name
car1=TyotaCar("Fortune")
car2=TyotaCar("RanitaCar")
print(car1.name)
print(car1.start())
print(car1.color)      
