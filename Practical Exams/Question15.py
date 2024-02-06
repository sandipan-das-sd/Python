# 15.	Write a Program in Python to find the GCD & LCM of two given numbers using function.
def gcd(a,b):
    if a<b:
        return b
    
    else:
        return gcd(b,a%b) 
    
def lcm(a,b):
    return a*b//gcd(a,b)

m=int(input("Enter the first number:-"))
n=int(input("Enter the second number:-"))
result1= gcd(m,n)
print("The gcd is",result1)

result2= lcm(m,n)
print("The lcm is ",result2)
