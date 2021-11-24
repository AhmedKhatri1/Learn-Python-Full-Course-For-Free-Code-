#Inner class

class Student: #Outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.laptop.show()

    class Laptop: #Inner Class
        def __init__(self):
            self.brand = "HP"
            self.processor = "i5"
            self.ram = 12
            self.ssd = 'SSD installed'
        def show(self):
            print(self.brand,self.processor,self.ram,self.ssd)

s1 = Student("Ahmed",1)
s2 = Student("Ali",2)
s1.show()
s2.show()
