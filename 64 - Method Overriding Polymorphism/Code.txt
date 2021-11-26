#method overriding
#same name, same parameter

# class A:
#     def show(self):
#         print("A class!")
#
# class B(A):
#     def show(self):
#         print("B class!")
#         pass
#
# a = B()
# a.show()

class Class_Room:
    def marks(self,marks):
        self.marks = marks
        return marks + 100
class Student_details(Class_Room):
    # pass
    def marks(self,marks):
        self.marks = marks
        return marks + 100

a = Student_details()
print(a.marks(70))

