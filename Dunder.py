class Employee:
    name = "Sandipan"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self) :
        return f"The name of the employee is{self.name}"
e = Employee()

# Display the value of the 'name' attribute
print(e.name)

# Display the length of the 'name' attribute using the custom __len__ method
print(len(e))
