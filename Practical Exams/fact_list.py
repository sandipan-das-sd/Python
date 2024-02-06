
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
factorial_sum = sum(factorial(i) for i in range(1, n+1))


factorial_terms = [f"{i}!" for i in range(n, 0, -1)]

# Print the result in the desired format
print("[", end=" ")
for term in factorial_terms:
    print(term, end=" ")
    if term != "1!":
        print("+", end=" ")
print(f"] = {factorial_sum}")
