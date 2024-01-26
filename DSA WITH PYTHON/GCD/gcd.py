#An algorithm for gcd(m,n)


#use fm,fn for list of factors of m,n respectively
# for each i from 1 to m ,add i to fm if i divides m 
# for each j from 1 to n ,add j to fn if j divides n
#Use cf for list of common factors 
#for each f in fm,add f to cf if f also appears in fn
#Return largest (rightmost) value in cf
#Return largest (rightmost) value in cf


# Code:


def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i)==0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
      if(n%j)==0:
          fn.append(j)
    cf=[] #cf denotes common factors
    for f in fm:
        if f in fn:
            cf.append(f)
    if len(cf)>0:
        return cf[-1]
    else:
        return 1 #if no common factor found ,gcd is 1
        
m=int(input("Enter the fiest no:-\n"))
n=int(input("Enter the second number:-\n"))
result= gcd(m,n)
print(f"The gcd is {result}")



