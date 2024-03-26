# Inheritance :

# 2. Multilevel Inheritance

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
        super().__init__(make, model, year)
        self.color = color

# Define a subclass named "ElectricCar" inheriting from "Car"
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity

# Create an instance of ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 2023, "Black", "100 kWh")

# Print the description of the electric car
print(my_electric_car.get_description())  # Output: 2023 Tesla Model S


# In this example:

# We have a superclass Vehicle and two subclasses Car and ElectricCar.
# The ElectricCar class inherits from Car, which in turn inherits from Vehicle.
# Each subclass inherits the attributes and methods of its superclass, forming a hierarchy.
