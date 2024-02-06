number=int(input('Enter the number to find factorial:-'))
step=[]
factorial=1
for i in range(number,0,-1):
    factorial*=i
    step.append(i)
print("The factorial is:-",factorial)
print("The step is:-",step)