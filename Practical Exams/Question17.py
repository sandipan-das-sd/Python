# 17.	Write a Python Program to Put Even and Odd elements of a List into Two Different Lists
count=int(input("How many  number you want to insert:-\n"))
even=[]
odd=[]
full_list=[]
print("Enter the element\n ")
for i in range(count):
    
    full_list.append(int(input()))
print(full_list)
 
for i in range(len(full_list)):
    if full_list[i]%2==0:
        even.append(full_list[i])
    else:
        odd.append(full_list[i])

print(even)
print(odd)

