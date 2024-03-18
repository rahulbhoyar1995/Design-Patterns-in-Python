# Inheritance :
# 3. Multiple Inheritance

# Define a superclass named "Animal"
class Animal:
    def speak(self):
        return "Animal speaks"

# Define another superclass named "Pet"
class Pet:
    def play(self):
        return "Pet plays"

# Define a subclass named "Dog" inheriting from both "Animal" and "Pet"
class Dog(Animal, Pet):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
my_dog = Dog()

# Print methods from both superclasses and subclass
print(my_dog.speak())  # Output: Animal speaks
print(my_dog.play())   # Output: Pet plays
print(my_dog.bark())   # Output: Dog barks


# In this example:

# We have two superclasses Animal and Pet, and a subclass Dog inheriting from both superclasses.
# The Dog class inherits methods from both Animal and Pet, allowing it to exhibit behaviors from both classes.
# These examples demonstrate different types of inheritance in Python, showcasing how subclasses can inherit properties and methods from their superclasses, promoting code reuse and establishing hierarchical relationships between classes.