# 1.Write a Program in Python to compute the Factorial of a Number using Recursion.
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)
    

n = int(input("Enter the number to compute the factorial: "))
print("The factorial is:", Factorial(n))
