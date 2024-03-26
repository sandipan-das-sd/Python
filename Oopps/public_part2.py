class Person:
    __name="Sandipan"
    def __hello(self):
        print("Hello Sandipan")
    def welcome(self):
        self.__hello()
p1=Person()
# print(p1.__name) #cant possible
# print(p1.__hello())# cant posssible
print(p1.welcome())