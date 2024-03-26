
# Here is the correct implementation :

class Patient:
    def __init__(self, name):
        self.name = name
        self.medications = []

    def add_medication(self, medication_name, dosage="As needed", frequency="As needed"):
        # Method to add medication with default or specified dosage and frequency
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


# Usage : 

# Method overloading in this context allows us to provide different interfaces for adding medications to a patient's record, catering to various use cases and providing convenience for the user. It enhances code readability and usability by allowing methods with similar functionalities to be grouped together under the same name.