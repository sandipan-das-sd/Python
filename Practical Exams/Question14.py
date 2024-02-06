# 14.	Write a Python program to reverse a tuple
# Initialize an empty tuple
my_tuple = ()

# Input the number of elements in the tuple
n = int(input("Enter how many numbers you want to add: "))

# Input the elements of the tuple
for i in range(n):
    # Append the elements to the tuple append function is not needed in tuple
    my_tuple += (int(input()),)

# Display the original tuple
print("The tuple is:", my_tuple)
print(my_tuple[::-1]) #another method
# Reverse the tuple
reversed_tuple = tuple(reversed(my_tuple))

# Display the reversed tuple
print("The reversed tuple is:", reversed_tuple)
