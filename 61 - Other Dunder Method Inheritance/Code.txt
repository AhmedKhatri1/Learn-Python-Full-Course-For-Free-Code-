#other dunder method inheritance
#magic methods,starting ending __
# __add__

class Number():
    def __init__(self,num):
        self.num = num
    def __add__(self, num2):
        print("Adding")
        return self.num + num2.num
    def __mul__(self, num2):
        print("Multiplying")
        return self.num * num2.num
    def __str__(self):
        return f"Decimal Number : {self.num}"
    def __len__(self):
        return 1

no = Number(1000)
print(no)
print(len(no))


