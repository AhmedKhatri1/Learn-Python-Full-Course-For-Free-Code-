#static method -- main reason is not to pass a self in our function

class Employee():
    salary = 50000 #class attribute/variable
    def get_phone_no(self):
        print("Number is : 123456789")
    def get_phone_no_1(self):
        print(f"Number is : {self.phone_no}")

    @staticmethod
    def abc():
        print("Welcome!")
    @staticmethod
    def time():
        print("The time is 12PM!")


a = Employee()
a.abc()
a.time()
a.get_phone_no()
a.phone_no = '12345'
a.get_phone_no_1()
print(a.salary)
a.salary = 100000 #instance attribute/variable
print(a.salary)