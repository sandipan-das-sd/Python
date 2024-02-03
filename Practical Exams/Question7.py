#7.	Write a Python program that creates a Dictionary, one that stores conversion value from meter to centimetre. 
n = int(input("How many numbers you want to convert from meter to centimeter: "))
print("Enter the numbers in meters to convert them to centimeters:")

my_dict = {}

for i in range(n):
    meter_value = float(input())
    centimeter_value = meter_value * 100
    my_dict[meter_value] = centimeter_value

print("Conversion from meter to centimeter:")
print(my_dict)
