# 5.	Write a Python program that take User's Name and Aadhaar Number. Validate the taken information using "isx()" function Print (Where 'x' is either Alpha or number , digit ). 

def isDigit(aadhar_number):
    if aadhar_number.isdigit() and len(aadhar_number) == 12:
        print("Valid Aadhar number")
        return True
    else:
        print("Invalid Aadhar number")
        return False

def isChar(aadhar_id):
    if aadhar_id.replace(" ", "").isalpha():
        print("Valid user name")
        return True
    else:
        print("Invalid user name")
        return False


def validate():
    aadhar_number = input("Enter the Aadhar number: ")
    aadhar_id = input("Enter the Aadhar name: ")

    if isDigit(aadhar_number) and isChar(aadhar_id):
        print("Aadhar details validated successfully!")
    else:
        print("Aadhar details validation failed.")

validate()
