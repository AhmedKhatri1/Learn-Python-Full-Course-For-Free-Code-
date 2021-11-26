#method overloading

class Student:
    def sum(self,a=None,b=None,c=None):
        s = 0

        if a!=None and b!=None and c!=None:
            s = a+b+c
            return s
        elif a!=None and b!=None:
            s=a+b
            return s
        elif a!=None:
            s=a
            return s
        else:
            return s

s1 = Student()
print(s1.sum())
print(s1.sum(10))
print(s1.sum(10,20))
print(s1.sum(10,20,30))