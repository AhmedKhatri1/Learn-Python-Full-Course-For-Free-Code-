class Helicopter:
    def fly(self):
        print("Helicopter is Flying!")
class Bee:
    def fly(self):
        print("Bee is Flying!")
class Athlete:
    def swim(self):
        print("He is swimming!")

for i in Helicopter(),Bee(),Athlete():
    i.fly()