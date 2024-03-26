# Define a class named "Employee" to represent an employee object

class Employee:
    num_of_employees = 0  # Class variable to store the total number of employees 

    def __init__(self, name, salary):
        # Instance variables representing attributes of each employee
        self.name = name      # Instance variable: Name of the employee
        self.salary = salary  # Instance variable: Salary of the employee

        # Increment the total number of employees when a new instance is created
        Employee.num_of_employees += 1  

    def display_employee_details(self):
        # Method to display the details of the employee
        return f"Name: {self.name}, Salary: ${self.salary}"

# Create instances of the Employee class
employee1 = Employee("John Doe", 50000)
employee2 = Employee("Jane Smith", 60000)

# Display the details of each employee
print("Employee 1 Details:", employee1.display_employee_details())
print("Employee 2 Details:", employee2.display_employee_details())

# Display the total number of employees
print("Total Number of Employees:", Employee.num_of_employees)  # Here num_of_employees is class variabel


# In this example:

# (A) Instance Variables:

# Each instance of the Employee class (employee1, employee2, etc.) has its own name and salary instance variables, representing the unique state of each employee object.
# Instance variables are associated with individual objects and store data specific to each object.


# (B) Class Variable:

# The num_of_employees class variable is shared among all instances of the Employee class.
# It represents a property that is common to all objects of the class.
# Class variables are defined within the class but outside of any method and are accessible to all instances of the class.
# Uses of Instance Variables:

# Differences : 

# Instance variables store data unique to each object, such as an employee's name and salary.
# They represent the state of individual objects and are used to store object-specific data.

# Uses of Class Variables:

# Class variables are used to store data shared among all instances of a class, such as a count of the total number of objects created from the class.
# They represent properties common to all objects of the class and are accessed using the class name itself (Employee.num_of_employees).





