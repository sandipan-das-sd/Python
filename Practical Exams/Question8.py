#9.	Write a Python program to convert a string to upper case letters using user-defined function.
lowerString=input("Enter the lower string\n")
#using nouser defined function
upperString=lowerString.upper()
print(upperString)

#using user defned function
def convert_to_lowercase(string):
    """Converts an uppercase string to lowercase."""
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            # Convert uppercase character to lowercase by adding 32 to its ASCII value
            result += chr(ord(char) -32 )
        else:
            result += char
    return result

lowerString = input("Enter the string: ")
lowerString = convert_to_lowercase(lowerString)
print("String in lowercase:", lowerString)