class Student:
    def __init__(self,name) :
        self.name=name
s1=Student("Sandipan")
print("Stuydent name before deletion",s1.name)
del s1
print("Student name after deletion",s1.name)
        