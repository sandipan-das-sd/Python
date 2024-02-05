import random 

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
list1 = []

# Use a set to store unique numbers
unique_numbers = set()

# Keep generating random numbers until we have enough unique numbers
while len(unique_numbers) < (end - start + 1):
    unique_numbers.add(random.randint(start, end))

# Convert the set to a list
list1 = list(unique_numbers)

print("The list is:\n", list1)
