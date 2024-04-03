# Interface Segregation principle

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
     