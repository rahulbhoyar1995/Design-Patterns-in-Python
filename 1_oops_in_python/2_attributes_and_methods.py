# Define a class named "Person" to represent an individual
class Person:
    def __init__(self, name, age, gender):
        # Initialize attributes for the person
        self.name = name  # Attribute: Name of the person
        self.age = age  # Attribute: Age of the person
        self.gender = gender  # Attribute: Gender of the person

    def introduce(self):
        # Method: Returns a formatted introduction of the person
        introduction = f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}."
        return introduction

    def celebrate_birthday(self):
        # Method: Increments the age of the person by 1 to celebrate their birthday
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    def change_name(self, new_name):
        # Method: Changes the name of the person to the given new name
        self.name = new_name
        print(f"Name updated successfully. New name: {self.name}")


# Create an instance of the Person class representing an individual
john = Person("John", 30, "Male")

# Call the introduce() method to introduce the person
print(john.introduce())

# Call the celebrate_birthday() method to celebrate John's birthday
john.celebrate_birthday()

# Call the change_name() method to change John's name
john.change_name("Johnny")

# Call the introduce() method again to introduce the person with the updated name
print(john.introduce())



# In this example:

# Attributes: The Person class has attributes such as name, age, and gender. These attributes represent the state of an individual, including their name, age, and gender.

# Methods: The Person class defines methods such as introduce, celebrate_birthday, and change_name. These methods define the behavior of a person object and operate on its attributes. For example:

# introduce method returns a formatted introduction of the person.
# celebrate_birthday method increments the age of the person by 1 to celebrate their birthday.
# change_name method changes the name of the person to the given new name.
