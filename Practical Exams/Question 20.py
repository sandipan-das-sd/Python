# Define the number of rows
rows = 5

# First pattern
print("5432112345")

# Second pattern
for i in range(1, rows):
    # Print the initial part of the second pattern
    print(" 543 ", end="")

    # Calculate the spacing between the two parts of the second pattern
    spaces = (2 * (rows - i - 1)) + 2

    # Print the space
    for _ in range(spaces):
        print(" ", end="")

    # Print the second part of the second pattern
    if i != rows - 1:
        print("2345")
    else:
        print("2345")  # Extra space for the last row
