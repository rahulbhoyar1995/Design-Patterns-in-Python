# Interface Segregation principle
#The Interface Segregation Principle (ISP) is one of the five SOLID principles of object-oriented programming. It states that clients should not be forced to depend on interfaces they do not use. In simpler terms, it suggests that it's better to have multiple specific interfaces for different parts of a system rather than a single large interface that covers everything.

#Let's break it down:

# Interfaces: In programming, an interface defines a contract for classes. It specifies what methods a class should have, but not how those methods should be implemented.
# Clients: In the context of ISP, "clients" are the classes or modules that use interfaces.
# Depend: When a class or module depends on an interface, it means that it relies on that interface to provide certain functionality.
# Forced: This means that the client is required to implement or use certain parts of an interface, even if it doesn't need them.
# Segregation: This term refers to separating or dividing. In the context of ISP, it means splitting interfaces into smaller, more specific parts.
# So, the Interface Segregation Principle suggests that instead of having one large interface that covers everything, it's better to have several smaller interfaces that are tailored to specific use cases. This way, clients can depend only on the interfaces that they actually need, rather than being forced to depend on unnecessary methods or functionality.

# For example, imagine you have an interface called Worker with methods like work() and eat(). If some classes only need to work() and don't care about eat(), they shouldn't be forced to implement or depend on the eat() method. Instead, you could have separate interfaces like Workable and Eatable, allowing classes to depend only on what they need.

# Following ISP helps keep codebases modular, maintainable, and easier to understand and modify. It also reduces the likelihood of unintended consequences when making changes to interfaces or implementations.

from abc import abstractmethod, ABC

class Machine:
    def print(self, document):
        raise NotImplementedError()
    
    def fax(self, document):
        raise NotImplementedError()
    
    def scan(self, document):
        raise NotImplementedError()
    
# ok if you need a multi-functional device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass
    
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass
    
    def fax(self, document):
        pass # Do nothing
    
    def scan(self, document):
        """Not supported"""
        raise NotImplementedError("Printer can not scanned!")
    
    
# printer = OldFashionedPrinter()
# printer.fax("21312")   #Nothing happens here
# printer.scan("234234")   # Ooops ....Error raised
 
        
    
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass
    
class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass
    
class MyPrinter(Printer):
    def print(self, document):
        print(f"Printing document is :{document}")
        
# printer_obj = MyPrinter()
# printer_obj.print("This is extraordinory document.")

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Printing using Photocopier : {document}")
        
    def scan(self, document):
        print(f"Scanning document using Photocopier : {document}")
        
# pc_obj = Photocopier()
# pc_obj.print("This is extraordinory document for printing.")
# pc_obj.scan("This is extraordinory document for scanning.")
      
class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass
    
    @abstractmethod
    def fax(self, document):
        pass
    
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner
        
    def print(self, document):
        self.printer.print(document)
        
    def scan(self, document):
        self.scanner.scan(document)
        
        
test_printer = Printer()
test_scanner = Scanner()

mfm = MultiFunctionMachine(test_printer,test_scanner)
mfm.print("Printing this using MultiFunctionMachine")
mfm.scan("Scanning this using MultiFunctionMachine")
     
