# 35.	Write a program to get the factorial of a number and the values has to be stored within a list. 
# Example: Suppose the number is 4 of which you want to find out the factorial.
# Output: The factorial of 4 is 24 and the steps are [4, 3, 2, 1]


def factorial_with_steps(num):
    factorial = 1
    steps = []

   
    for i in range(num, 0, -1):
        factorial *= i
        steps.append(i)

    return factorial, steps
'''
in the for loop here num is staring point 
0 is ending point 
and -1 is steps of the loop of the next itretion
'''

number = int(input("Enter a number to find its factorial: "))


result, steps = factorial_with_steps(number)


print("The factorial of", number, "is", result, "and the steps are", steps)
