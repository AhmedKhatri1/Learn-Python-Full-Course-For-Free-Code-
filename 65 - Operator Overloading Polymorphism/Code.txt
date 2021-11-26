#operator overloading

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d) " % (self.a,self.b)

    def __add__(self, other):
        return Vector(self.a + other.a,self.b,other.b)

a1 = Vector(-5,5)
b1 = Vector(-10,11)
print(a1)
print(b1)

