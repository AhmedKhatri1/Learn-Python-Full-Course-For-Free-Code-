#polymorphism
#Shape - circle,triangle,square in outer world

class Cow:
    def __init__(self,str):
        self.name = str
    def greet(self):
        print("I'm Deisy!")
class Mice:
    def __init__(self,str):
        self.name = str
    def greet(self):
        print("I'm Jerry!")
class Dog:
    def __init__(self,str):
        self.name = str
    def greet(self):
        print("I'm Tommy!")
class Cat:
    def __init__(self,str):
        self.name = str
    def greet(self):
        print("I'm Tom!")

total_animal = [Cow("Mo Mo"),Cat("Meow Meow"),Dog("Wo Wo"),Mice("xyz"),Cat("cat is meow")]

for i in total_animal:
    i.greet()
