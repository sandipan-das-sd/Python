class Employee:
    def __init__(self, name):  # Constructor for the Employee class
        self.name = name  # Assigning the name attribute

class Dancer:
    def __init__(self, dance):  # Constructor for the Dancer class
        self.dance = dance  # Assigning the dance attribute

#multiple inheritance
        
class DancerEmployee(Employee, Dancer):  # DancerEmployee class inheriting from Employee and Dancer
    def __init__(self, dance, name):  # Constructor for the DancerEmployee class
        self.dance = dance  # Assigning the dance attribute
        self.name = name  # Assigning the name attribute

o = DancerEmployee("Kathak", "Ranita")  # Creating an instance of DancerEmployee
print(o.name)  # Printing the name attribute of the instance
print(o.dance)  # Printing the dance attribute of the instance
