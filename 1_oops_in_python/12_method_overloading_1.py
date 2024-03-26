# Method overloading :

# It refers to the ability to define multiple methods with the same name but with different parameters within a class. 

# While Python does not support method overloading in the traditional sense (as in languages like Java or C++), we can achieve similar functionality by using default arguments or variable-length argument lists. 

# Method overloading is useful when we want to provide multiple ways to call a method with different sets of parameters.

# Let's consider an example from the healthcare domain, where we have a class called Patient that represents a patient's medical record. We'll implement a method called add_medication to add medications to the patient's record. We'll demonstrate method overloading by providing different ways to call this method based on the number of parameters passed.

class Patient:
    def __init__(self, name):
        self.name = name
        self.medications = []

    def add_medication(self, medication_name, dosage, frequency):
        # Method to add medication with specified dosage and frequency
        medication_info = {'name': medication_name, 'dosage': dosage, 'frequency': frequency}
        self.medications.append(medication_info)

    def add_medication(self, medication_name, dosage):
        # Method to add medication with specified dosage (default frequency assumed)
        frequency = "Once daily"  # Default frequency
        medication_info = {'name': medication_name, 'dosage': dosage, 'frequency': frequency}
        self.medications.append(medication_info)

    def add_medication(self, medication_name):
        # Method to add medication without specifying dosage and frequency
        dosage = "As needed"  # Default dosage
        frequency = "As needed"  # Default frequency
        medication_info = {'name': medication_name, 'dosage': dosage, 'frequency': frequency}
        self.medications.append(medication_info)

# Creating a patient record
patient1 = Patient("John Doe")

# Adding medications using different method calls
patient1.add_medication("Aspirin")  # Adding medication without specifying dosage and frequency
patient1.add_medication("Ibuprofen", "200mg")  # Adding medication with specified dosage
patient1.add_medication("Acetaminophen", "500mg", "Twice daily")  # Adding medication with specified dosage and frequency

# Displaying the patient's medications
print(f"Patient: {patient1.name}")
print("Medications:")
for med in patient1.medications:
    print(f"- {med['name']}: Dosage - {med['dosage']}, Frequency - {med['frequency']}")


# In this example:

# We define three versions of the add_medication method within the Patient class, each with a different number of parameters. This demonstrates method overloading.

# The first version of add_medication takes three parameters (medication name, dosage, and frequency).

# The second version takes two parameters (medication name and dosage), with the frequency assumed to be "Once daily" by default.

# The third version takes only one parameter (medication name), with both dosage and frequency assumed to be "As needed" by default.

# We create a Patient object and add medications using different method calls to demonstrate the flexibility of method overloading.


# You will get error here :
# The error you're encountering is likely related to the fact that Python does not support method overloading in the same way as languages like Java or C++. In Python, only the latest definition of a method with a particular name in a class will be retained, effectively overwriting any previous definitions.

# In your Patient class, you've defined the add_medication method three times, each time with a different set of parameters. However, only the last definition will be used, and the earlier ones will be overridden. Hence, when you try to call the method with different parameter counts, Python expects the latest definition (which accepts only one parameter) and raises an error if you try to call it with more.

# To achieve similar functionality to method overloading in Python, you can use default parameter values or variable-length argument lists (e.g., *args or **kwargs).

# You will see its implementation in the next file.
 
