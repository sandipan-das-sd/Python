# Algorithm for gcd⁡(m,n)
# To find the largest common factor, start at the end and 
# work backwards
# Let i run from min(m,n) to 1
# First common factor that we find will be ged!


#Euclid's algorithm

# Suppose d divides both m and n, and m>n
# Then m=ad,n=bd
# So m-n=ad-bd=(a-b)d
# d divides m-n as well!
# So gcd⁡(m,n)=gcd⁡(n,m-n)

# Consider gcd⁡(m,n) with m>n
# If n divides m, return n
# Otherwise, compute gcd⁡(n,m-n) and return that value

#code:
def gcd(m, n):
    # Assume m >= n
    if m < n:
        (m, n) = (n, m)
    if (m % n) == 0:
        return n
    else:
        diff = m - n
        # diff > n? possible!
        return gcd(max(n, diff), min(n, diff))

# Example usage:
m = 24
n = 36
result = gcd(m, n)
print(f"The gcd of {m} and {n}  by Euclids algorithm is {result}")

'''
Algorithm Process
-------------------


1. Initial check: `m` (24) is not 
less than `n` (36), so we don't swap them.

2. The condition `(m % n) == 0` is not
 satisfied, so we calculate the difference `diff = m - n`,
   which is 24 - 36 = -12.

3. The recursive call is made
 with the arguments `max(n, diff)` and `min(n, diff)`,
which are `max(36, -12)` and `min(36, -12)` respectively. 
This translates to `gcd(36, -12)`.

4. Now, the algorithm repeats 
with the new values. Since 36 is not less than -12,
 the values are swapped: `(m, n) = (-12, 36)`.

5. The condition `(m % n) == 0`
 is still not satisfied, so we calculate 
 the new difference `diff = m - n`, which is -12 - 36 = -48.

6. The recursive call is
 made again with the arguments `max(n, diff)` and `min(n, diff)`,
   which are `max(36, -48)` and `min(36, -48)` respectively. This translates to `gcd(36, -48)`.

7. This process continues until
 `(m % n) == 0` is satisfied. 
 In this example, it stops when the values are `(0, 12)`.

8. The last non-zero remainder,
 which is 12, is returned as the gcd.

The final output of the code will be:
 "The gcd of 24 and 36 is 12". 
 The code successfully finds the
 greatest common divisor using the Euclidean algorithm.



 Even better


Suppose n does not divide m
Then m=qn+r,
where q is the quotient, 
r is the remainder when we divide m by n
Assume d divides both m and n
Then m=ad,n=bd
So ad=q(bd)+r
It follows that r=cd, so d divides r as well

Improved Version of Euclids Algorithm

Consider gcd(m,n) with m>n
If n divides m, return n
Otherwise, let r=m%n
Return gcd(n,r)






'''
#Update euclid's algorithm code

def gcd(m, n):
    if m < n:  # Assume m >= n
        (m, n) = (n, m)
    if (m % n) == 0:
        return n
    else:
        return gcd(n, m % n)  # m % n < n, always!
# Example usage:
m = 24
n = 36
result = gcd(m, n)
print(f"The gcd of {m} and {n}  by Euclids algorithm Updated is {result}")
'''
Efficiency

Can show that the second version of Euclid's algorithm
 takes time proportional to the number of digits in m
If m is 1 billion (10^9 ),
 the naive algorithm takes billions of steps,
 but this algorithm takes tens of steps

'''