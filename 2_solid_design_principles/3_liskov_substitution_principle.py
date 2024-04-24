# The Liskov Substitution Principle (LSP) 
# It is a fundamental concept in object-oriented programming that states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In simpler terms, it means that a subclass should behave in such a way that it can be substituted for its superclass without altering the desired behavior of the program.

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
        
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f"Width: {self._width}, Height: {self._height}"
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._width
    
    @height.setter
    def height(self, value):
        self._height = value
        

class Sqaure(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self,value):
        _width = _height = value
        
    @Rectangle.height.setter
    def height(self,value):
        _width = _height = value
        
        
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")
    

rc = Rectangle(2, 3)
use_it(rc)

sq = Sqaure(5)
use_it(sq)        

# In the provided example, we have a Rectangle class and a Square class, where Square is a subclass of Rectangle. Let's analyze how this example adheres to or violates the Liskov Substitution Principle:

# Subtyping Relationship: The Square class is clearly a subtype of the Rectangle class, as a square can be seen as a special case of a rectangle where all sides are of equal length. This relationship is a good indicator that LSP might be applicable.

# Inheritance: The Square class inherits from the Rectangle class, which is a correct use of inheritance. However, the way properties are overridden might violate LSP.

# Property Overrides: In the Square class, the width and height properties are overridden with setters that attempt to set both width and height to the same value. This approach violates the LSP because it alters the behavior of the Rectangle class. In a rectangle, changing one dimension should not automatically change the other dimension, but in the Square class, it does. This means that substituting a Square object for a Rectangle object can lead to unexpected behavior.

# Violation of Expectations: The use_it function demonstrates a violation of LSP. When it's called with a Rectangle object, it correctly calculates the area after changing the height, but when called with a Square object, it doesn't behave as expected because changing the height also changes the width due to the overridden setter methods in the Square class.

# In summary, while the Square class inherits from the Rectangle class, the way it overrides properties violates the Liskov Substitution Principle. To adhere to LSP, subclasses should not change the behavior of their superclass in a way that surprises users of the superclass.


########################################################################


print("-"*100)
print("Corrected Implementation :")


########################################################################
# To adhere to the Liskov Substitution Principle (LSP), we need to ensure that substituting a Square object for a Rectangle object does not alter the expected behavior of the program. In the context of geometric shapes, this means that a Square should still behave like a Rectangle, but with additional constraints due to its specialized nature.

# One way to modify the code to adhere to LSP is to reconsider the design of the Square class. Instead of directly inheriting from the Rectangle class and overriding its methods, we can create a separate Shape class that both Rectangle and Square inherit from. This way, we can define common behavior for both shapes without violating LSP.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle: Width = {self.width}, Height = {self.height}"

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size * self.size

    def __str__(self):
        return f"Square: Size = {self.size}"

def use_it(shape):
    shape.width = 5  # Modifying width for testing purposes
    shape.height = 10
    expected = 50
    print(f"Expected an area of {expected}, got {shape.area()}")

rectangle = Rectangle(2, 3)
use_it(rectangle)

square = Square(5)
use_it(square)


# In this modified version:

# Both Rectangle and Square inherit from a common Shape class, which provides a common interface for calculating the area.

# Each shape class (Rectangle and Square) implements its own area method according to its specific formula.

# The use_it function takes a Shape object as an argument and tests it by setting its width and height, then calculating and printing the area. This function works correctly regardless of whether the object passed to it is a Rectangle or a Square, demonstrating adherence to the Liskov Substitution Principle.

# By separating concerns and providing a common interface through the Shape class, we ensure that both Rectangle and Square can be used interchangeably without altering the expected behavior of the program.
