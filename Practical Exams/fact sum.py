
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
factorial_sum = sum(factorial(i) for i in range(1, n+1))


for i in range(n, 0, -1):
    print(f"{i}!", end=" ")
    if i != 1:
        print("+", end=" ")

print(f"= {factorial_sum}")
