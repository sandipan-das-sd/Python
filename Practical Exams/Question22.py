# 22.	Write a Python program to find out the Lateral Surface Area of a Right Cylinder, Volume of a Right CircularCone [r=10cm, h=20cm].
#lateral surface of the right circular cone
import math
r=int(input("Enter the radius of the right circular cone:-\n"))
h=int(input("Enter the height of the right circular cone:-\n"))
area= (math.pi)*r*(math.sqrt(r**2+h**2))
print("The area of right circular cone is :-\n",area, "square unit")
''' You can ignore the upper part'''

''' The answer is start from here '''
''' Calculating the area'''
lat_sur_area_rightcylinder=2*math.pi*r*h
print("The area of the right cylinder is:-\n",lat_sur_area_rightcylinder,"square_unit")

''' Calculating the volume'''
rightcylinder_volume=1/3*(math.pi)*(r**2)*h
print("The volume of right cylinder is:\n",rightcylinder_volume,"cubic _unit")
