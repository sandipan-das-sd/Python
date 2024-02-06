start = int(input("From where you want to check the automorphic number: "))
end = int(input("Up to which you want to check the automorphic number: "))

# Iterate through the numbers in the given range
automorphic_numbers = []

for num in range(start, end + 1):
    square = num ** 2
    if str(square).endswith(str(num)):
        automorphic_numbers.append(num)

print("The automorphic number list is:", automorphic_numbers)

# Check if a specific number is automorphic
num_to_check = int(input("Enter a number to check if it's automorphic: "))
if num_to_check in automorphic_numbers:
    print("The number", num_to_check, "is automorphic.")
else:
    print("The number", num_to_check, "is not automorphic.")
