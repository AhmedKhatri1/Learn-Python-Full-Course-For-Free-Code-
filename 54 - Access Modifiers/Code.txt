#access modifiers

class Test:
    testPublic = 1
    _testProtected = 2
    __testPrivate = 3

    def public_method(self):
        print("Public Method")
    def protected_method(self):
        print("Portected Method")
    def private_method(self,mobile_number):
        print("Private Method")

class SubClass(Test):
    pass

a = SubClass()
print(a.testPublic)
print(a._testProtected)
print(a.__testPrivate)
