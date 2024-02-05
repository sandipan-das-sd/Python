# 40. Write a program in python to find the result of the following y: 
# 𝑦= (𝑎+𝑏)^3÷(𝑐−𝑑)×(𝑎∗𝑏∗𝑐)/(𝑎−𝑏−𝑐) 
# Where a = 3; b = 2; c = 10; d = 5

a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
c=int(input("Enter the value of c:-"))
d=int(input("Enter the value of d:-"))


y = ((a + b) ** 3) / ((c - d) * (a * b * c) / (a - b - c))


print('The result is: {:.2f}'.format(y))
