class Number():
    def __init__(self,num):
        self.num = num
    def __add__(self, num2):
        print("Adding")
        return self.num + num2.num
    def __mul__(self, num2):
        print("Multiplying")
        return self.num * num2.num

no_1 = Number(2)
no_2 = Number(5)
sum = no_1 + no_2
print(sum)

mul = no_1 * no_2
print(mul)
