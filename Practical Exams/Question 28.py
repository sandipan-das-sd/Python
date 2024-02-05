# 28.	Python Program using  function to Find LCM of two numbers.
def gcd(m,n):
    if m<n:
        return n
    else:
        return (m,n%m)
def lcm(a,b):
    return a*b//gcd(a,b)
p = int(input("Enter the first number: "))
q = int(input("Enter the second number: "))



result2 = lcm(p, q)
print("The LCM is:", result2)

