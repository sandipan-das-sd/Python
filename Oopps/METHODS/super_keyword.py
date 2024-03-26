# Base class: Employee
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Derived class: Programmer (inherits from Employee)
class Programmer(Employee):
    def __init__(self, name, id, lang):
        # Call the constructor of the base class (Employee) using super()
        super().__init__(name, id)
        self.lang = lang

# Create an Employee object 'Sandipan'
Sandipan = Employee("Sandipan", "121")

# Create a Programmer object 'Ranita'
Ranita = Programmer("Ranita", "111", "Python")

# Display details of the Employee and Programmer objects
print("Class Employee details are:", Sandipan.name, Sandipan.id)

# Display details of the Programmer object, including the inherited attributes from Employee
print("Programmer Class Details are:", Ranita.name, Ranita.id, Ranita.lang)

# Using super() to access attributes of the base class (Employee) in the derived class (Programmer)
print("\nUsing Super keyword")
print("Employee name:", Sandipan.name)
print("Employee id:", Sandipan.id)
# 'lang' attribute is not available in the Employee class, so it will result in an AttributeError
# Uncommenting the line below would result in an error:
# print("Employee programming language:", Sandipan.lang)
