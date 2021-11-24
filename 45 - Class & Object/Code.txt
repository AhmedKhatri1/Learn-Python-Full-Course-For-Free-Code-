class Student:
    def student_info(self):
        print("Ahmed","Ali","Asad","Zaheer")
    def student_info2(self):
        print("Rashid","Moiz","Asim","Zaid")

stud_1 = Student()
stud_2 = Student()

Student.student_info(stud_1) #calling function, using class and object name
Student.student_info2(stud_2)

stud_1.student_info() #using object itself to call the function
stud_1.student_info2()
