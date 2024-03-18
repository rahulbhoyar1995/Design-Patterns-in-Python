# Single Responsibility Principle
# This principle states that a class should have only one reason to change. In other words, it should have only one responsibility.

class Journal:
    def __init__(self):
        # Initialize the journal entries and count
        self.entries = []
        self.count = 0
        
    def add_entry(self, text):
        # Add a new entry to the journal
        self.entries.append(f"{self.count} :{text}")
        self.count += 1
    
    def remove_entry(self, pos):
        # Remove an entry from the journal based on its position
        del self.entries[pos]
        
    def __str__(self):
        # Convert journal entries to a string
        return "\n".join(self.entries)
    
# The journal class should handle only the single responsibility of storing the data.
# To handle file operations, we create a new class called "PersistenceManager".
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, file_name):
        # Save journal entries to a file
        with open(file_name, 'w') as file:
            file.write(str(journal))
        
# Creating an instance of the Journal class
j = Journal()
j.add_entry("I cried today")
j.add_entry("I was feeling alive")

print(f"Journal entries:\n{j}")

print("-" * 50)

# Creating an instance of the PersistenceManager class to save the journal entries to a file
p = PersistenceManager()
file_name = "files/journal.txt"
p.save_to_file(j, file_name)

# Verifying the data from the saved file
print("Fetching the data from the file:")
with open(file_name) as fh:
    print(fh.read())

# Applying Single Responsibility Principle by separating concerns into distinct classes.
