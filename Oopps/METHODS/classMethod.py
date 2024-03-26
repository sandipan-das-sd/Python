'''
To acces the attributes from the class we use class attributes
'''

class Person:
    name="aanynomus"
    # def changeName(self,name): #attributes
        # self.name=name
        # Person.name=name #2nd way
        # self.__class__.name=name #3rd way 
        # '''
        # we access the name from the class methods
        # '''
        # '''
        # Now if we want under the function we directly access the class then?
        # '''
    @classmethod
    def changeName(cls,name):
        cls.name=name
    
p1=Person()
p1.changeName("Sandipan ")
print(p1.name)
print(Person.name)

'''
When i try to change class attribute name then
it cant change but in case of normal 
attribute it chnages
'''

