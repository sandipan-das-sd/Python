# 25.	Python Program to make a list with each item being increasing 
# power of 2.
# import math
list=[]
n= int(input("Enter how many item you want to inser:-\n"))

for i in range(n):
    ele=2**i
    
    list.append(ele)
print("The list is:-\n",list)

