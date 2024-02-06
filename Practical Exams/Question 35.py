number = int(input("Enter a number to find its factorial: "))

factorial = 1
steps = []

for i in range(number, 0, -1):
    factorial *= i
    steps.append(i)

print("The factorial of", number, "is", factorial, "and the steps are", steps)
