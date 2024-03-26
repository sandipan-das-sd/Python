'''
super() method used to access method of the parent class
when we call super() then all the method are comes from the class here the class is Car when we call super then  all the method like starts and stops are comes and when we calles __init__ then all the  constructior under the class is caled and when we call __init__(type) then the type constructor are comes 
'''

class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car Started")
    @staticmethod
    def stop():
        print("car Stopped")

class Tyotacar(Car):
    def __init__(self, name,type):
        self.name=name
        # self.type=type
        super().__init__(type)
car1=Tyotacar("Sandipan","electric")
print(car1.type)
        