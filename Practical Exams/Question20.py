# Write a program to print the following pattern 
# 5432112345
# 5432  2345
# 543    345
# 54      45
# 5        5



rows = 5

for i in range(rows):
    # Print numbers decreasing from 5 to (5 - i)
    for j in range(rows, rows - i, -1):
        print(j, end='')
    
    # Print spaces
    for _ in range(2 * i):
        print(' ', end='')

    # Print numbers increasing from (6 - i) to 5
    for k in range(rows - i, rows + 1):
        print(k, end='')
    
    print()  # Move to the next line
