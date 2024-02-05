# Write a Python program to reverse a tuple.
new_tuple = ()
n = int(input("How many elements do you want to insert: "))
print("Enter the elements: ")
for i in range(n):
    ele = int(input())  
    new_tuple += (ele,)  
#reversed is only used for list not in tuple. To use reversed function in tuple we have to convert the tuple to list 
reversed_tuple=new_tuple[::-1]
print("The tuple is", new_tuple)
print('The reverse of the tuple is:-',reversed_tuple)