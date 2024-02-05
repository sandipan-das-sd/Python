# 21.	Write a Python program to compute the real roots of a quadratic equation ax2+bx+c=0.
import math

a = int(input("Enter the coefficient of a:-\n"))
b = int(input("Enter the coefficient of b:-\n"))
c = int(input("Enter the coefficient of c:-\n"))

d = b**2 - 4*a*c

if d == 0:
    print("The roots are real and equal ")
    print("The root is:", -b / (2*a))
elif d > 0:
    print("The roots are real but unequal:-")
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are:", root1, root2)
else:
    print("No real roots. The roots are complex")
