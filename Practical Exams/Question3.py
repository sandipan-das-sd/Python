#3.	Write a Program in Python for determining whether a number is a Pearson number or not. 
# (e.g. 145 is a Pearson number because 1! + 4! + 5! =145.)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_Pearson(number):
    original_number = number
    sum_of_factorials = 0

    while number > 0:
        digit = number % 10
        sum_of_factorials += factorial(digit)
        number //= 10

    return original_number == sum_of_factorials

number = int(input("Enter the number: "))

if is_Pearson(number):
    print(f"{number} is a Pearson number.")
else:
    print(f"{number} is not a Pearson number.")
