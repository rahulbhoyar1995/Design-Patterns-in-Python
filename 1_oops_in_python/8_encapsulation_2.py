# Define a class named "Employee" to represent an employee object
class Employee:
    def __init__(self, name, salary):
        # Initialize attributes for the employee
        self.name = name  # Public attribute: Name of the employee
        self.__salary = salary  # Private attribute: Salary of the employee
        self._department = "HR"  # Protected attribute: Department of the employee (initialized to "HR")

    def display_name(self):
        # Public method: Display the name of the employee
        return f"Employee Name: {self.name}"

    def __display_salary(self):
        # Private method: Display the salary of the employee
        return f"Employee Salary: ${self.__salary}"

    def _display_department(self):
        # Protected method: Display the department of the employee
        return f"Employee Department: {self._department}"


# Create an instance of the Employee class
employee1 = Employee("John Doe", 50000)

# Access public attributes and methods
print(employee1.display_name())  # Output: Employee Name: John Doe
# print(employee1.__salary)  # Error: AttributeError: 'Employee' object has no attribute '__salary'
# print(employee1.__display_salary())  # Error: AttributeError: 'Employee' object has no attribute '__display_salary'

# Access protected attribute and method (not recommended, just for demonstration)
print(employee1._department)  # Output: HR
print(employee1._display_department())  # Output: Employee Department: HR

# Access private attribute and method (not recommended, just for demonstration)
# print(employee1.__salary)  # Error: AttributeError: 'Employee' object has no attribute '__salary'
# print(employee1.__display_salary())  # Error: AttributeError: 'Employee' object has no attribute '__display_salary'


# In this example:

# Public Attributes/Methods: 
# The name attribute and the display_name method are public. 
# They can be accessed and used from outside the class.

# Private Attributes/Methods: 
# The __salary attribute and the __display_salary method are private. 
# They are indicated by prefixing with double underscores __. Private attributes and methods are intended to be accessed and used only within the class itself.

# Protected Attributes/Methods: 
# The _department attribute and the _display_department method are protected. They are indicated by prefixing with a single underscore _. Protected attributes and methods are conventionally considered private, but they can still be accessed from outside the class. However, it's recommended not to access them directly from outside the class to maintain encapsulation.