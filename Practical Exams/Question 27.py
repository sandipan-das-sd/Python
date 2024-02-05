# 27.	 Python Program using recursive function to Find HCF or GCD of two  numbers
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def hcf(a, b):
    return gcd(a, b)

p = int(input("Enter the first number: "))
q = int(input("Enter the second number: "))

result1 = gcd(p, q)
print("The GCD is:", result1)

result2 = hcf(p, q)
print("The HCF is:", result2)
