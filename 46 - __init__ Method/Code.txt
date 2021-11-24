#Init method

class Mobile:
    #using init method
    def __init__(self,ram,rom):
        self.ram = ram
        self.rom = rom
    def configuration(self):
        print("Configuration is :",self.ram,self.rom)

mob_1 = Mobile(4,16)
mob_2 = Mobile(8,64)

mob_1.configuration()
mob_2.configuration()
