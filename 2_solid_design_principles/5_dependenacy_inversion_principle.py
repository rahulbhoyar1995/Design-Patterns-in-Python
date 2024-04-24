# Dependecy Inversion Principle

# High-level modules should not depend on low-level modules: In traditional programming, higher-level modules often depend directly on lower-level modules. For example, a business logic module might directly depend on a database access module. This creates tight coupling, making it difficult to change or replace either module without affecting the other.
# Both high-level and low-level modules should depend on abstractions: Instead of depending on specific implementations, modules should depend on interfaces or abstract classes. This allows for interchangeable components. Going back to the previous example, the business logic module would depend on an interface for data access rather than a specific database access module.
# Abstractions should not depend on details: The interfaces or abstract classes used for dependencies should not be tied to specific implementations or details. They should define what functionality is needed without dictating how it's implemented. This allows for different implementations to be used interchangeably.
# By following the Dependency Inversion Principle, you make your code more flexible, maintainable, and easier to test. It promotes modular design and makes it easier to swap out components without affecting the rest of the system

from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2
    
class Person:
    def __init__(self,name):
        self.name = name
    
    
class RelationshipBrowser:    # Interface introduced 
    @abstractmethod
    def find_all_children_of(self, name):
        pass
    
class Relationships(RelationshipBrowser): # Low lavel
    relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
        
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name  == name and r[1] == Relationship.PARENT:
                yield r[2].name
                
                
class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g storage type
    
    # def __init__(self, relationships):
    #     relations = relationships.relations
        
    #     for r in relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}.")
    
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}.")
            
            
parent  = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

# Low level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
