#can we do better?

#we scan from 1 to m to complete the fm and again from 1 to n to complete fn
#why not a single scan from 1 to max(m,n)??
# for each i in 1 to max (m,n) add i to fm if i divides m and add i to fn if i divides n

#Even better??
#why compute two lists and then compare them to compute common factors cf?Do it in one shot
#for each i in 1 to max(m,n) ,if i divides m and i also divides n,then add i to cf

#actually ,any common factor must be less than min(m,n)
#for each i in 1 to min(m,n),if i divides m and i also divides n,then add i to cf

#code:
def gcd(m, n):
    cf = []
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            cf.append(i)
    return cf[-1]

# Example usage:
m = 24
n = 36
result = gcd(m, n)
print(f"The gcd of {m} and {n} is {result}")

#Example:-


# In this example, the loop runs from 1 to the minimum of 
# m and n (which is 24), 
# and it finds all common factors of 24 and 36.
# The last (rightmost) element in the cf list will be
# the greatest common divisor, which is 12 in this case 
# (1, 2, 3, 4, 6, 12 are common factors of 24 and 36).


#Why cf[-1]??

# In the context of the code, cf[-1] 
# is used to access the last element of 
# the list cf. In Python, negative indices
# are used to count elements from the end of the list.
# So, cf[-1] refers to the last element, cf[-2] would refer to the
# second-to-last element, and so on.

# In this example, when the loop finds
# common factors and appends them to the cf list, the
# return cf[-1] statement returns the last (rightmost) 
# element of the list,
# which is the greatest common divisor (gcd) of 24 and 36.

# In this specific case, the cf list 
# would contain [1, 2, 3, 4, 6, 12], 
# and cf[-1] would be equal to 12, which is the gcd of 24 and 36.

#Do we need list at all??

#we only need the largest common factor
#1 will alawys be a common factor
#Each time we find a larger common factor,discard the previous one
#REMEMBER THE LARGEST COMMON factor seen so far and return it
#mcf-- most recent common factor

#Code with NO lists!
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if(m%i)==0 and (n%i)==0:
            mcf=i
        return (mcf)
# Example usage:
m = 24
n = 36
result = gcd(m, n)
print(f"The gcd of {m} and {n}  with NO Lists is {result}")

#Scan backwards??

#To find the largest common factor,start at the end at the end and work backwords
#let i run from min(m,n)to 1
#First common factor that we find will be gcd

#Scan Backwords Code:

def gcd(m, n):
    i=min(m,n)
    while i>0:
        if(m%i)==0 and (n%i) ==0:
            return(i)
        else:
            i=i-1
# Example usage:
m = 24
n = 36
result = gcd(m, n)
print(f"The gcd of {m} and {n}  with Scan Backwords with No lists is {result}")

# The goal is to decrement i in each iteration
# to go through all possible values.

# The loop condition should check if i > 0
# because you want to iterate until i becomes zero.

# This method uses a while loop to 
# iteratively check for common factors
# and decrease the value of i until it finds the
# greatest common divisor. The loop runs until i is a 
# common factor of both m and n. 
# Once a common factor is found,
# the loop terminates, and the common factor (gcd) is returned.


# A new kind of repetition


# while condition:
# step 1
# step 2
# step k
# Don't know in advance how many times we will repeat the steps
# Should be careful to ensure the loop terminates eventually
#  the condition should become false!




