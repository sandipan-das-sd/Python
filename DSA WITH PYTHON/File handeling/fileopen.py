try:
    f = open("demofile.txt", "w")
    print("File opened successfully!")
    # Additional operations with the file can be performed here
except IOError:
    print("An error occurred while opening the file.")
f = open("demofile.txt", "rt")