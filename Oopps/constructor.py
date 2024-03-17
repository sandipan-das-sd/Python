class Student:
    name="Sandipan Das"
    def __init__(self) :
        print(self)
        print("Adding new student in the database... ")
   


s1=Student()
print(s1.name)
print(s1)
#s1 object and self are same thing self is pointing to the object s1
#self alwyas pointing to the first parameter 
'''
<__main__.Student object at 0x000001F3589EDBD0>
Adding new student in the database...
Sandipan Das
<__main__.Student object at 0x000001F3589EDBD0>  
PS F:\coding\Python>
'''

#second programe
class Student:
    
    def __init__(self,fullname) :
        # print(self)
        self.name=fullname

        print("Adding new student in the database... ")
   


s1=Student("Ranita")
print(s1.name)
s2=Student("arjun")
print(s2.name)

#Third programe
class Student:
    
    def __init__(self,name,marks) :
        # print(self)
        self.name=name
        self.marks=marks

        print("Adding new student in the database... ")
   


s1=Student("Ranita",98)
print(s1.name)
print(s1.marks)
s2=Student("arjun",99)
print(s2.name)
print(s2.marks)