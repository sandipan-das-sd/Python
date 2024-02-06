aadhar_number = input("Enter the Aadhar number: ")
aadhar_id = input("Enter the Aadhar name: ")

# Validate Aadhar number
if aadhar_number.isdigit() and len(aadhar_number) == 12:
    print("Valid Aadhar number")
else:
    print("Invalid Aadhar number")

# Validate user name
if aadhar_id.replace(" ", "").isalpha():
    print("Valid user name")
else:
    print("Invalid user name")

# Check if both Aadhar number and user name are valid
if aadhar_number.isdigit() and len(aadhar_number) == 12 and aadhar_id.replace(" ", "").isalpha():
    print("Aadhar details validated successfully!")
else:
    print("Aadhar details validation failed.")
