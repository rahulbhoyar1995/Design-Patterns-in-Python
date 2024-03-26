# Abstraction : 

# Abstraction in Python involves hiding the complex implementation details of a class while providing a simple interface for interacting with it. 

# This allows programmers to focus on using the class without worrying about its internal complexities. 

# Abstraction is essential for creating clean and maintainable code by promoting separation of concerns and reducing dependencies.

from abc import ABC, abstractmethod

# Define an abstract class named "Shape" to represent geometric shapes
class Shape(ABC):  # Using ABC (Abstract Base Class) module to create abstract classes
    def __init__(self, name):
        self.name = name  # Attribute: Name of the shape

    @abstractmethod
    def area(self):
        # Abstract Method: Calculates the area of the shape
        pass

    @abstractmethod
    def perimeter(self):
        # Abstract Method: Calculates the perimeter of the shape
        pass

# Define a concrete subclass of Shape called "Rectangle"
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width  # Attribute: Width of the rectangle
        self.height = height  # Attribute: Height of the rectangle

    def area(self):
        # Method: Calculates the area of the rectangle (implementation specific to rectangle)
        return self.width * self.height

    def perimeter(self):
        # Method: Calculates the perimeter of the rectangle (implementation specific to rectangle)
        return 2 * (self.width + self.height)

# Define a concrete subclass of Shape called "Circle"
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius  # Attribute: Radius of the circle

    def area(self):
        # Method: Calculates the area of the circle (implementation specific to circle)
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        # Method: Calculates the circumference of the circle (implementation specific to circle)
        return 2 * 3.14 * self.radius

# Create instances of Rectangle and Circle
rectangle = Rectangle("Rectangle", 5, 4)
circle = Circle("Circle", 3)

# Using abstraction to calculate area and perimeter without knowing internal details
print(f"{rectangle.name} Area:", rectangle.area())  # Output: Rectangle Area: 20
print(f"{rectangle.name} Perimeter:", rectangle.perimeter())  # Output: Rectangle Perimeter: 18
print(f"{circle.name} Area:", circle.area())  # Output: Circle Area: 28.26
print(f"{circle.name} Circumference:", circle.perimeter())  # Output: Circle Circumference: 18.84


# In this example:

# The Shape class is an abstract base class defining common methods area and perimeter that all shapes should implement. This class hides the implementation details of these methods, allowing concrete subclasses to provide their own implementations.

# The Rectangle and Circle classes are concrete subclasses of Shape that implement specific shapes. They provide their own implementations of area and perimeter methods, hiding the details of calculations internally.

# The Rectangle and Circle classes expose only the essential features (area and perimeter methods) to the users, abstracting away the implementation details. Users can interact with these classes without knowing how the area and perimeter calculations are performed internally.

# Abstraction helps in promoting code reuse, reducing complexity, and enhancing maintainability by separating the interface from the implementation. 

# It allows programmers to work with high-level concepts (shapes in this case) without getting bogged down by low-level details.