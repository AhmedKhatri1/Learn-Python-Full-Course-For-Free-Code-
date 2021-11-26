#We make this to create our own abstract classes
#They are the methods in which they have only declaration not a definition
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Mobile(Computer):
    def process(self):
        print("Mobile is running!")

class Programmer():
    def programmer(self,comp):
        print("Programmer is solving problems")
        comp.process()

# comp_1 = Computer()
mob_1 = Mobile()
prog_1 = Programmer()
prog_1.programmer(mob_1)

