#6.	Write a Python program to convert a Tuple of string values to a Tuple of integer values.
n = int(input("Enter the total number of elements to be inserted in the tuple: "))
Tupple = ()
print("Enter the strings to the tuple:")

for i in range(n):
    element = input()
    Tupple += (element,) 

new_Tupple = () 

for item in Tupple:
    try:
       
        new_Tupple += (int(item),)
    except ValueError:
        print(f"Unable to convert {item} to an integer. Skipping...")

print("Tuple of integer values:", new_Tupple)

