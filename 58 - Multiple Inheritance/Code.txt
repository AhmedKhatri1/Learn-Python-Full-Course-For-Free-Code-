class Company(): #base class
    level = 0
    company = "ahmed.com"

    def level_upgrade(self):
        self.level = self.level + 1

class Employee(): #base class
    company = "khatri.com"

class Programmer(Company,Employee): #derived/child class
    name = "Ahmed"

p = Programmer()
print(p.level)
p.level_upgrade()
print(p.level)
print(p.name)
print(p.company)
print(Programmer.company)
print(Employee.company)


