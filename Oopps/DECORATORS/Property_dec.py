'''
We use @property decorator on any method in the class to
 use the method as a property
 here percantage is a just a attribute when the attribute value depends on a function then
   we use propertyh method
'''


class Student:
    def __init__(self,phy,chem,math) :
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percenatage=str((self.phy+self.chem+self.math)/3)+"%"

        # def calculatePercanatge(self):
        #     self.percenatage=str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percenatage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1=Student(100,90,95)
print(stu1.percenatage)

'''
Now if we think that the phy marks will be mistakenly written as 90 it will be 80 then we cant change the marks and avg value
percantage will not change
'''
stu1.phy=86
'''
we dont have to call the extra another method when the ,marks chnage the perventage changes autometiaclly

'''
print("Physics markes chnaged to",stu1.phy)
# stu1.calculatePercanatge()
print("Now the percanatge is ",stu1.percenatage)

