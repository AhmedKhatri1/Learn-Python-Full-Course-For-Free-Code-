#Abstract class must have atleast one method in class

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def print(self):
        print("Abstract Class!")

    @abstractmethod
    def print_abstract(self):
        pass

class ChildClass(AbstractClass):
    def print(self):
        print("Child Class! - Normal Method")
    def print_abstract(self):
        print("Child Class! - Abstract Method")

a = ChildClass()
a.print()
a.print_abstract()
