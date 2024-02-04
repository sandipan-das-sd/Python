# 16.	Write a python program read a string as input. If the input string contains only alphabet  characters then print ASCII value of each character otherwise display an error message.

str1=str(input("Enter a string:-"))
if str1.isalpha():
    for char in str1:
        print("Ascii value of {char} is ",ord(char))
else:
    # If the string contains non-alphabet characters, display an error message
    print("Error: Input string contains non-alphabet characters.")
    