# 26.	Python Program to make a list of odd numbers within a range
m=int(input("From where you want to start to find the odd no:-\n"))
n=int(input("Up to which you want to  find the odd number:-\n"))
odd=[]
for i in range(m,n+1):
    if i % 2 != 0:
        odd.append(i)
print("The odd number is",odd)

