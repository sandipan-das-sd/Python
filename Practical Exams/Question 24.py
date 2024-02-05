# 24.	 Write a program in python to print the following pattern:
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

rows=int(input("Enter the number of rows:-\n"))
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print() # to move the next line


'''



```python
for j in range(5, 0, -1):
    print(j, end=' ')
```

In this loop:
- `j` starts at 5 (`i` is assumed to be 5 here, for demonstration).
- It decrements by 1 in each iteration (`-1` as the step value).
- The loop continues until it reaches 0, but does not include 0.

Here's how the loop runs:

1st iteration: `j` is 5.
2nd iteration: `j` is 4.
3rd iteration: `j` is 3.
4th iteration: `j` is 2.
5th iteration: `j` is 1.

The loop stops after the 5th iteration because it does not include 0 in the range. Therefore, the output of this loop would be: `5 4 3 2 1`.

'''

