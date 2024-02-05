# 38.  Write a program to find out the cumulative sum of a list. [ List should be taken from user]
n=int(input("Enter how many you want to insert:-"))
sum=0
list1=[]
print("Enter the element;-")
for i in range(n):
    ele=int(input())
    list1.append(ele)
print("The list is :-",list1)
print("The summation is:-")
for num in range(len(list1)):
    sum+=list1[num]
print(sum)