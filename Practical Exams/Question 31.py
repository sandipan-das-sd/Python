# 31.	Write a Python program to convert a tuple into a dictionary.
new_tuple = ()
n = int(input("How many elements do you want to insert: "))
print("Enter the elements: ")
for i in range(n):
    ele = input()  
    new_tuple += (ele,)  

print("The tuple is", new_tuple)

new_dict = {}
for i in range(0, len(new_tuple), 2):
   if i + 1 < len(new_tuple):
        key = new_tuple[i]
        value = new_tuple[i + 1]
        new_dict[key] = value

print("The dictionary is:", new_dict)
