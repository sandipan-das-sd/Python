#Hirerarchical Inheritance
'''
CEO 
   
   |
------------
|    |     |
m1   m2    m3
'''
class BaseClass:
    pass  # Base class with no specific attributes or methods


class D1(BaseClass):
    pass  # Derived class 1 inheriting from BaseClass


class D2(BaseClass):
    pass  # Derived class 2 inheriting from BaseClass


class D3(D1):
    pass  # Derived class 3 inheriting from D1


# In this example, D1, D2, and D3 inherit from the BaseClass.
# D3 also inherits from D1, creating a hierarchical inheritance structure.

# This means that D1, D2, and D3 inherit attributes and methods from the BaseClass.
# D3 additionally inherits attributes and methods from D1, forming a hierarchy where D3 is a specialized version of D1.
