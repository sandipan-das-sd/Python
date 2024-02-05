#9.	Write a Python program to convert a string to lower case letters using user-defined function.
upperString=input("Enter the upper string\n")
#using system  defined function
lowerString=upperString.lower()
print(lowerString)

#using user defned function
def convert_to_lowercase(string):
    """Converts an uppercase string to lowercase."""
    result = "" #store the lower case in the result 
    for char in string:  
        if 'A' <= char <= 'Z':
            # Convert uppercase character to lowercase by adding 32 to its ASCII value
            result += chr(ord(char) +32 )
        else:
            result += char
    return result

upperString= input("Enter the string: ")
upperString = convert_to_lowercase(upperString)
print("String in lowercase:", upperString)