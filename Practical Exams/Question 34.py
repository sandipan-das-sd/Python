# 34.	Write a program to create two lists as the square and cube of the elements of the given list.
n = int(input("How many numbers do you want to insert: "))
my_list = []

print("Enter the elements:")
for i in range(n):
    ele = int(input())
    my_list.append(ele)

def square(lst):
    square_lst = []
    for i in range(len(lst)):
        square_lst.append(lst[i]**2)
    return square_lst

def cube(lst):
    cube_lst = []
    for i in range(len(lst)):
        cube_lst.append(lst[i]**3)
    return cube_lst

square_list = square(my_list)
cube_list = cube(my_list)
print("The original list is:", my_list)
print("List of Squares:", square_list)
print("List of Cubes:", cube_list)
