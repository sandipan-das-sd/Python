# 37.  Create a list entre random numbers within a range. Then Multiply the odd and even numbers separately and store the result within a list. Example: Input = [1,2,3,4,5]
# Output = [15,8]


import random 

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
list1 = []
unique_numbers = set()

# Generate unique random numbers
while len(unique_numbers) < (end - start + 1):
    unique_numbers.add(random.randint(start, end))
list1 = list(unique_numbers)
print("The list is", list1)

my_list = []
odd_product = 1
even_product = 1

for num in list1:
    if num % 2 == 0:
        even_product *= num
    else:
        odd_product *= num

my_list = [odd_product, even_product]

print("The modified list is:", my_list)

'''
[1,3,5]
even no 1,3,5
1*3*5=15
5
1*1=1
1*3=3
3*5=15
even_product=



'''