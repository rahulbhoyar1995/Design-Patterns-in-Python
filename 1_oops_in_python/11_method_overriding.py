# Method overriding :
# It is a concept in object-oriented programming where a subclass provides a specific implementation of a method that is already defined in its superclass. 
 
# This allows the subclass to customize or extend the behavior of inherited methods. 

# Method overriding is particularly useful when you want to provide a different implementation of a method in a subclass while maintaining the method signature and interface


# Define a superclass named "FinancialInstrument"
class FinancialInstrument:
    def __init__(self, principal, rate):
        # Initialize principal amount and interest rate
        self.principal = principal
        self.rate = rate

    def calculate_interest(self):
        # Method to calculate interest (generic implementation)
        return self.principal * self.rate

# Define a subclass named "SavingsAccount" that inherits from "FinancialInstrument"
class SavingsAccount(FinancialInstrument):
    def calculate_interest(self):
        # Method overriding: Calculate interest for a savings account
        return self.principal * self.rate / 12  # Monthly interest calculation

# Define another subclass named "FixedDeposit" that inherits from "FinancialInstrument"
class FixedDeposit(FinancialInstrument):
    def calculate_interest(self):
        # Method overriding: Calculate interest for a fixed deposit
        return self.principal * self.rate * 2  # Annual interest calculation

# Instantiate objects of SavingsAccount and FixedDeposit classes
savings_account = SavingsAccount(principal=1000, rate=0.05)
fixed_deposit = FixedDeposit(principal=10000, rate=0.08)

# Calculate interest for each financial instrument
savings_interest = savings_account.calculate_interest()
fixed_deposit_interest = fixed_deposit.calculate_interest()

# Display the calculated interest
print(f"Savings Account Interest: ${savings_interest}")
print(f"Fixed Deposit Interest: ${fixed_deposit_interest}")


# In this example:

# We have a superclass named FinancialInstrument representing a generic financial instrument with an __init__ method to initialize the principal amount and interest rate, and a calculate_interest method to calculate the interest based on the principal and rate.
# We define two subclasses, SavingsAccount and FixedDeposit, representing specific types of financial instruments (e.g., savings account and fixed deposit).
# Each subclass overrides the calculate_interest method with a specific implementation tailored to its type of financial instrument. For example, the SavingsAccount class calculates monthly interest, while the FixedDeposit class calculates annual interest.
# When we instantiate objects of the SavingsAccount and FixedDeposit classes and call the calculate_interest method on them, the overridden method in each subclass is executed, providing the specific interest calculation for each type of financial instrument.



# Uses of Method Overriding:

# Customize behavior: Method overriding allows subclasses to provide custom implementations of methods inherited from superclasses, enabling customization of behavior based on specific requirements.
# Enhance functionality: Subclasses can extend or enhance the functionality of inherited methods by providing additional logic or features.
# Polymorphism: Method overriding facilitates polymorphism, where objects of different classes can be treated interchangeably based on their common superclass. This promotes code flexibility and reusability.