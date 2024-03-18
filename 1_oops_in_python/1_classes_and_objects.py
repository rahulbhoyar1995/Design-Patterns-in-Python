# Define a class named 'Car' to represent a blueprint for creating car objects

class Car:
    # Constructor method (__init__) initializes the object with default values
    def __init__(self, make, model, year):
        # Attributes to represent the state of the car object
        self.make = make  # Make of the car (e.g., Toyota, Honda)
        self.model = model  # Model of the car (e.g., Camry, Civic)
        self.year = year  # Year of manufacture

    # Method to display information about the car
    def display_info(self):
        # Print information about the car using its attributes
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


# Create an object of the 'Car' class representing a specific car
# This object is an instance of the 'Car' class
# We pass arguments to the constructor to initialize the object with specific values
my_car = Car("Toyota", "Camry", 2020)

# Call the display_info() method on the 'my_car' object to display information about the car
my_car.display_info()



# Explanation with comments:

# We define a class named Car using the class keyword. This class serves as a blueprint for creating car objects.
# Within the class definition, we define a constructor method __init__() that initializes the object with default values for its attributes (make, model, year).
# The self parameter in the constructor refers to the instance of the class itself and is used to access attributes and methods within the class.
# Inside the constructor, we initialize the attributes (make, model, year) of the object using values passed as arguments during object creation.
# We define a method display_info() within the class to display information about the car object. This method prints the values of the attributes (make, model, year) of the car.
# Outside the class definition, we create an object named my_car of the Car class. This object represents a specific car (in this case, a Toyota Camry manufactured in 2020).
# During object creation, we pass arguments ("Toyota", "Camry", 2020) to the constructor to initialize the object with specific values.
# We call the display_info() method on the my_car object to display information about the car, which prints the values of its attributes (make, model, year).
