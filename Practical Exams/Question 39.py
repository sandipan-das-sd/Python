# 39. Write a program in python to print the name of first 3 students on the basis of the following condition: 
# a) Total = in between (80 – 85) % the student is declared as 3rd 
# b) Total = in between (85 – 90) % the student is declared as 2nd 
# c) Total = >90 %, the student is declared as 1st 
# (Take the input for 3 students and also take the inputs for 3 subjects each named as English, Bengali and Math. Calculate the percentage and print the result according to their rank.)
# Function to calculate percentage

def calculate_percentage(english, bengali, math):
    total_marks = english + bengali + math
    percentage = (total_marks / 300) * 100
    return percentage


def determine_rank(percentage):
    if percentage > 90:
        return "1st"
    elif 85 <= percentage <= 90:
        return "2nd"
    elif 80 <= percentage < 85:
        return "3rd"
    else:
        return "Undefined"


students = []
for i in range(3):
    print(f"\nEnter details for student {i+1}:")
    english = int(input("Enter marks in English: "))
    bengali = int(input("Enter marks in Bengali: "))
    math = int(input("Enter marks in Math: "))
    percentage = calculate_percentage(english, bengali, math)
    rank = determine_rank(percentage)
    students.append((rank, percentage, f"Student {i+1}"))


sorted_students = sorted(students, reverse=True)
print("\nTop 3 students:")
for rank, percentage, student in sorted_students[:3]:
    print(f"{student} secured {percentage:.2f}% and is declared as {rank} rank.")
 
