# 36.  Write a program to get all the automorphic number within a given range. 
start = int(input("From where you want to check the automorphic number: "))
end = int(input("Up to which you want to check the automorphic number: "))

def is_automorphic(num):
    square = num ** 2
    str_num = str(num)
    str_square = str(square)
    return str_square.endswith(str_num)

# Create a list to store automorphic numbers
automorphic_number_list = []

for num in range(start, end + 1):
    if is_automorphic(num):
        automorphic_number_list.append(num)


print("The automorphic number list is:", automorphic_number_list)

num_to_check = int(input("Enter a number to check if it's automorphic: "))
if num_to_check in automorphic_number_list:
    print("The number", num_to_check, "is automorphic.")
else:
    print("The number", num_to_check, "is not automorphic.")
