# Inheritance :
# 1. Single Inheritance

# Define a superclass named "Vehicle"
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

# Define a subclass named "Car" inheriting from "Vehicle"
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        # Call the constructor of the superclass
        super().__init__(make, model, year)
        self.color = color

    def get_description(self):
        # Override the method from the superclass
        return f"{self.year} {self.make} {self.model}, Color: {self.color}"

# Create an instance of Car
my_car = Car("Toyota", "Corolla", 2022, "Red")

# Print the description of the car
print(my_car.get_description())  # Output: 2022 Toyota Corolla, Color: Red


# In this example:

# We have a superclass Vehicle with attributes make, model, and year, along with a method get_description.
# The subclass Car inherits from Vehicle and adds an additional attribute color.
# The Car class overrides the get_description method to include the color of the car.