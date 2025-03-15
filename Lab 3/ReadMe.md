# Multiple Inheritance in Python & Method Resolution Order (MRO)

## Multiple Inheritance
Python allows a class to inherit from multiple parent classes, enabling code reuse and flexibility. However, it can lead to complexities when methods with the same name exist in multiple parent classes.

## Method Resolution Order (MRO)
MRO determines the sequence in which Python looks for methods in a class hierarchy. It follows the **C3 Linearization (or C3 MRO)** algorithm, ensuring a consistent and predictable order.

- The `mro()` method or `__mro__` attribute can be used to check a class's MRO.  
- MRO follows the **Depth-First, Left-to-Right** approach while ensuring that each parent class is only searched once.

### Example
```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

print(D.mro())  # Displays the MRO sequence
d = D()
d.show()  # Calls the method from B since it's first in MRO
```

### Key Points
- Python resolves methods from left to right as per class declaration (`D(B, C) → B first, then C`).
- The `super()` function follows the MRO.
- MRO prevents the **Diamond Problem** by ensuring a class is not visited multiple times in an inconsistent order.

---

# Dictionary Comprehension Example

Dictionary comprehension allows the creation of dictionaries in a concise way using a single line of code.

### Example
```python
# Create a dictionary with squares of numbers from 1 to 5
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

# Composition: Car and Engine Classes

Composition is a design principle where one class contains an instance of another class instead of inheriting from it.

### Implementation
```python
class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.horsepower} HP {self.fuel_type} engine"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def display_info(self):
        return f"{self.make} {self.model} with {self.engine}"

# Creating an Engine object
engine1 = Engine("petrol", 150)

# Creating a Car object with the Engine instance
car1 = Car("Toyota", "Corolla", engine1)

# Testing the functionality
print(car1.display_info())  
# Output: Toyota Corolla with 150 HP petrol engine
```

### Key Takeaways
- The `Engine` class is a separate entity with its own attributes.
- The `Car` class **contains** an `Engine` instance instead of inheriting from it.
- This approach improves modularity and reusability.

---

# Vector Class with Dunder Methods

### Implementation
```python
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2))
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range. Use 0 for x and 1 for y.")

# Example usage:
v1 = Vector(2, 4)
v2 = Vector(3, 1)
print(v1)          # Output: Vector(2, 4)
print(v1 + v2)     # Output: Vector(5, 5)
print(v1 - v2)     # Output: Vector(-1, 3)
print(v1 * 3)      # Output: Vector(6, 12)
print(v1 == Vector(2, 4))  # Output: True
print(len(v1))     # Output: 4 (r