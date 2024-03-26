class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()

# Create an instance of the Shape class
rec = Shape(3, 5)
C = Circle(5)

# Call the area method by adding parentheses to get the result
print("Rectangle Area:", rec.area())
print("Circle Area:", C.area())
