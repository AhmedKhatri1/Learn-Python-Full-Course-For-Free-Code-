#OOP Concepts

class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self,name,id,salary):# special method called constructor
        self.__name = name
        self.__id = id
        self.__salary = salary

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_salary(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary

ak = Employee("Ahmed",1,50000)
print(ak.get_name())
print(ak.get_id())
print(ak.get_salary())
ak.set_name("Ali")
print(ak.get_name())
print(ak.get_id())
print(ak.get_salary())
