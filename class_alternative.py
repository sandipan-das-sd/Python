# Define a class named 'Employee'
class Employee():
    # Constructor method to initialize the object with name and salary
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Class method to create an Employee object from a string
    @classmethod
    def fromRanita(cls, string):
        # Split the input string into name and salary using '-' as a delimiter
        return cls(string.split("-")[0], string.split("-")[1])

# Create an Employee object 'Employee1' with name 'Sandipan' and salary '50000000'
Employee1 = Employee("Sandipan", "50000000")

# Display details of Employee1
print("Details of Employee1")
print(Employee1.name)
print(Employee1.salary)

# Define a string 'Ranita' representing Employee2's data
Ranita = "Ranita-5000000"

# Create an Employee object 'Employee2' using the class method 'fromRanita'
Employee2 = Employee.fromRanita(Ranita)

# Display details of Employee2
print("Details of Employee2")
print(Employee2.name)
print(Employee2.salary)

#Comments:
#1. Define a class named 'Employee' to represent an employee with name and salary attributes.
#2. Inside the class, create a constructor method '__init__' to initialize the object with name and salary.
#3. Define a class method 'fromRanita' to create an Employee object from a string in the format "name-salary".
#4. Create an Employee object 'Employee1' with name 'Sandipan' and salary '50000000'.
#5. Display the details of 'Employee1'.
#6. Define a string 'Ranita' representing Employee2's data in the format "Ranita-5000000".
#7. Create an Employee object 'Employee2' using the class method 'fromRanita' and passing the 'Ranita' string.
#8. Display the details of 'Employee2'.
