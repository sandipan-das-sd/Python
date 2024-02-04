# 18.	Write a python program to remove a key from the dictionary
# Initialize an empty dictionary
my_dict = {}

# Input the number of keys and their values in the dictionary
n = int(input("Enter how many keys you want to add to the dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

# Display the dictionary
print("Dictionary:", my_dict)

# Input the key to delete
delete_key = input("Which key you want to delete: ")

# Check if the key exists in the dictionary
if delete_key in my_dict:
    # If the key exists, remove it from the dictionary
    del my_dict[delete_key]
    print("Dictionary after deletion:", my_dict)
else:
    print("Key not found in the dictionary.")
