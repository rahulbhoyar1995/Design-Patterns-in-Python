# Define a class named "Student" to represent a student object
class Student:
    def __init__(self, name, age):
        # Initialize attributes for the student
        self.name = name  # Attribute: Name of the student
        self.age = age  # Attribute: Age of the student
        self.__grades = []  # Private attribute: List to store student's grades (encapsulated)

    def add_grade(self, grade):
        # Method: Add a grade to the student's list of grades
        self.__grades.append(grade)

    def get_grades(self):
        # Method: Get the list of grades for the student
        return self.__grades


# Create a new student object
student1 = Student("Alice", 20)

# Add grades for the student using the public method
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(75)
student1.add_grade(100)

# Attempting to directly access the private attribute '__grades' will result in an AttributeError
# print(student1.__grades)

# Accessing the list of grades using the public method 'get_grades'
grades = student1.get_grades()

# Display the student's grades
print(f"{student1.name}'s Grades: {grades}")



# In this example:

# Encapsulation: The Student class encapsulates the data (attributes) and methods within a single unit. The attributes name and age represent the state of a student object, while the private attribute __grades hides the internal state (list of grades) from direct access outside the class.

# Private Attribute: The __grades attribute is marked as private by prefixing it with double underscores (__). This convention in Python indicates that the attribute should not be accessed directly from outside the class, promoting encapsulation.

# Public Methods: The add_grade and get_grades methods provide controlled access to the private attribute __grades. These methods allow users to add grades to the student's list of grades and retrieve the list of grades, respectively.

