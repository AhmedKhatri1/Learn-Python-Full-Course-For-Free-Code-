#Pillar Of OOP
#encapsulation
#bulk of data -- few hide - totally hide
#data hiding

class Car:
    def __init__(self):
        self.speed = 10 #public method
        self.__speed_limit = 100 #private method
    def get_speed(self):
        return self.speed
    def set_speed_limit(self,new_speed_limit):
        self.__speed_limit = new_speed_limit
    def get_speed_limit(self):
        return self.__speed_limit

s = Car()
print(s.speed)
s.speed = 50
print(s.speed)
print(s.get_speed_limit())
s.__speed_limit = 150
print(s.get_speed_limit())
s.set_speed_limit(150)
print(s.get_speed_limit())