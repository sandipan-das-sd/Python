
try:

    # Open file "demopy.txt" in write mode
    f = open("demopy.txt", "w")
    print("File opened successfully!")

    # Additional operations with the file can be performed here
    f.write("Welcome to File opening")

    # Open file "demopy.txt" in append mode
    f = open("demopy.txt", "a")
    f.write("\nThis is an additional line.")

    # Read and print contents of file "demofile2.txt"
    f = open("demofile2.txt", "r")
    print(f.read())

except IOError:
    print("An error occurred while opening the file.",IOError)
