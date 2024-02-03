#2.	Write a Program in Python for determining whether a number is an Armstrong number or not(e.g. 153 is an Armstrong number because 13 + 53 + 33 = 153.).

def Armstrong(n):
    sum_of_cubes = 0
    
    
    # Calculate the sum of cubes of digits
    while n > 0:
        digit = n % 10
        sum_of_cubes += digit ** 3
        n //= 10

    return sum_of_cubes

n = int(input("Enter the number: "))
sum_result = Armstrong(n)

if n == sum_result:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
