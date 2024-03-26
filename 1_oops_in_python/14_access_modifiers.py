# Define a class named "Product" to represent a product in an E-commerce system

class Product:
    def __init__(self, name, price):
        # Public attributes accessible from outside the class
        self.name = name     # Public attribute: Name of the product
        self._price = price  # Protected attribute: Price of the product (indicated by single underscore)

    def get_price(self):
        # Method to get the price of the product
        return self._price

    def set_discount(self, discount):
        # Method to set a discount on the product price
        if discount >= 0 and discount <= 100:
            self._price -= (self._price * discount / 100)
        else:
            print("Invalid discount percentage!")

# Create an instance of the Product class
product1 = Product("Laptop", 1000)

# Accessing public attribute (name) directly
print("Product Name:", product1.name)

# Accessing protected attribute (_price) directly

# While Python allows accessing protected attributes, it is conventional to access them through getter and setter methods
print("Product Price:", product1._price)

# Accessing protected attribute using getter method
print("Product Price (via Getter):", product1.get_price())

# Setting discount on the product price
product1.set_discount(10)
print("Product Price after 10% discount:", product1.get_price())

# In this example:

# Access Modifiers: 
# 
# The _price attribute is designated as protected by prefixing it with a single underscore. This convention indicates that _price should be considered a non-public attribute, and its access should be restricted to within the class or its subclasses. However, Python does not enforce this restriction, and accessing protected attributes directly is allowed.

# Uses:

# Public Attributes: Attributes such as name are accessible from outside the class and can be accessed directly.

# Protected Attributes: Attributes such as _price are meant to be accessible only within the class or its subclasses. While Python allows direct access to protected attributes, it is a convention to access them through getter and setter methods for better encapsulation and abstraction.

# By following access modifiers conventions, developers can effectively control the visibility and accessibility of class members, enhancing encapsulation and maintaining code integrity.