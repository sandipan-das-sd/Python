# 30.	Python Program using function to Find Factors of Number.
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)

n=int(input("Enter the number to print the factorial of ths number:-\n"))
result=factorial(n)
print("The factorial is ",result)