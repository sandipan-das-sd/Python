class A:
    varA="Welcome to class A"
class B:
    varB="Welcome class B"
class C (A,B):
    varC="welcome to class C"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
