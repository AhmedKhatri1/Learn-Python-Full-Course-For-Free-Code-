#Multilevel inheritance

class Person: #parent/base class for employee class
    salary = 50000
    def taking_breath(self):
        print("I'm a person!")

class Employee(Person): #child class of person and parent/base class for programmer
    salary = 70000
    def taking_breath(self):
        print("I'm an Employee!")

class Programmer(Employee): #child class of employee
    salary = 80000

per = Person()
per.taking_breath()
emp = Employee()
emp.taking_breath()
prg = Programmer()
prg.taking_breath()
print(prg.salary)
print(emp.salary)
print(per.salary)