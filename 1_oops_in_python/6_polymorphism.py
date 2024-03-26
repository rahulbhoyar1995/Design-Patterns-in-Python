# Define a superclass named "Animal"
class Animal:
    def make_sound(self):
        # Method: Define a generic sound for all animals
        pass

# Define a subclass named "Dog" inheriting from "Animal"
class Dog(Animal):
    def make_sound(self):
        # Method: Define a specific sound for dogs
        return "Woof!"

# Define another subclass named "Cat" inheriting from "Animal"
class Cat(Animal):
    def make_sound(self):
        # Method: Define a specific sound for cats
        return "Meow!"

# Define a function that accepts any object of the "Animal" superclass
def animal_sound(animal):
    # Method: Call the "make_sound" method of the given animal object
    return animal.make_sound()

# Create instances of the "Dog" and "Cat" classes
dog = Dog()
cat = Cat()

# Call the "animal_sound" function with different animal objects
print("Dog says:", animal_sound(dog))  # Output: Dog says: Woof!
print("Cat says:", animal_sound(cat))  # Output: Cat says: Meow!


# In this example:

# Polymorphism: The Animal superclass defines a method make_sound, which serves as a generic behavior for all animals. Both Dog and Cat subclasses inherit from the Animal superclass and override the make_sound method with specific implementations for dogs and cats, respectively.

# The animal_sound function demonstrates polymorphism by accepting any object of the Animal superclass as an argument. It then calls the make_sound method of the given animal object. Despite being of different classes (Dog or Cat), both dog and cat objects are treated as objects of the common superclass Animal.

# When animal_sound function is called with dog and cat objects, it dynamically dispatches the appropriate make_sound method based on the actual type of the object passed. This enables flexible and extensible code, allowing different subclasses to provide their own implementations of common methods defined in the superclass.