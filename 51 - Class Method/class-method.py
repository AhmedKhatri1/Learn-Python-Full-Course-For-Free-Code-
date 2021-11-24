#class method

class Employee():
    salary = 50000
    company = "Hyperstar"

    @classmethod
    def change_salary(cls,sal):
        cls.salary = sal
    @classmethod
    def mesaage(cls):
        print("The company is : %s"%cls.company)

a = Employee()
print(a.company)
print(a.salary)
print(Employee.salary)
a.change_salary(100000)
print(a.salary)
print(Employee.salary)