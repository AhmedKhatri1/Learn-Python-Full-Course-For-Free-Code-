#inheritance
#base class -- derived/child class

class Employee(): #base class
    company = "Apple"

    def show_details(self):
        print("This is an employee!")

class Programmer(Employee): #derived/child class
    language = "Python"

    def get_languages(self):
        print(f"The language is : {self.language}")
    def show_details(self):
        print("This is programmer!")

e = Employee()
e.show_details()
print("The company is :",e.company)
p = Programmer()
p.show_details()
print("The company is :",e.company)

e.company = "Facebook"
print("Now,the company is :",e.company)
print("The company of the programmer is :",p.company)
p.get_languages()


