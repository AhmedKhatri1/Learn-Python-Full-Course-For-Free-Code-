#Constructor

class Employee():
    salary = 100
    company = "Hyperstar"

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        print(f"The name of the employee is : {self.name}")
        print(f"The age of the employee is : {self.age}")
        print(f"The salary of the employee is : {self.salary}")

    @staticmethod
    def abc():
        print("Welcome!")
    @staticmethod
    def time():
        print("The time is 12PM!")

print("The salary of employee using public method is :",Employee.salary)
a = Employee("Ali",30,300000)
a.abc()
a.time()
a.get_details()
# print(Employee.salary)
print("The company is :",Employee.company)
