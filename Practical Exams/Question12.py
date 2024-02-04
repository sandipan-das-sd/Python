# 12.	Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def are_all_primes(numbers):
    for num in numbers:
        if num <= 1:
            return False  # Numbers less than or equal to 1 are not prime
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False  # If the number is divisible by any other number, it's not prime
    return True

# Input the numbers from the user
num_count = int(input("How many numbers do you want to check? "))
user_data = []

print("Enter the numbers:")
for i in range(num_count):
    user_data.append(int(input()))

# Check if all numbers are prime
print(f"{user_data} -> {are_all_primes(user_data)}")
