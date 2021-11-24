#Getter setter

class Uni:
    def __init__(self,course_name):
        self.coursename = course_name
    def set_course_name(self,course_name):
        self.coursename = course_name.upper()
    def get_course_name(self):
        return(self.coursename)

a = Uni("Java")
print("The course name is :",a.get_course_name())
a.set_course_name("Python")
print("Now, the course name is :",a.get_course_name())
# print(a.get_course_name())
