#multithreading

from threading import *
from time import sleep

class Ahmed(Thread):
    def run(self):
        for i in range(3):
            print("Ahmed")
            sleep(1)

class Khatri(Thread):
    def run(self):
        for i in range(3):
            print("Khatri")
            sleep(1) #must have to set time in threading

a1 = Ahmed() #a1 is a object of Ahmed
a2 = Khatri() #a2 is a object of Khatri

a1.start()
sleep(0.1)
a2.start()

a1.join()
a2.join()

print("Tata! Bye Bye! Khatam!")