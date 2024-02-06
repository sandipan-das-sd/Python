# #11.	Write a Program in Python to Generate the Fibonacci Series up to Nth Term.
# # 1+ 1 + 2 + 3 + 5 + 8 + 13 + . . . . + Nth Term

n = int(input("Enter up to which term you want to print the Fibonacci number: "))
# Initialize first two terms
a = 0
b = 1
sum = 1

if n <= 0:
    print("Enter a positive number\n")
elif n == 1:
    print(a)
    sum = 0
else:
    print(a, "+", b, end=" ")  # Print the first two terms
    # Fibonacci series
    for i in range(2, n):
        next_term = a + b
        print("+", next_term, end="")
        sum += next_term  # Update the sum
        # Update the next terms for the next iteration
        a, b = b, next_term

    print("=", sum)
n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci = [0, 1]
for _ in range(n - 2):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci[:n])

