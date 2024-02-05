n=int(input("Enter the number of terms:-\n"))
list=map(lambda x: 2**x,range(n))
#x is equal to each itretion of the numbers
print("The list of power of 2 is:\n")
for power in list:
    print(power)
