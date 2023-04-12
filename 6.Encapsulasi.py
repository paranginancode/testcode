# Encapsulasi adalah buat semua variable private
# getter untuk mengambil variable
# setter untuk mengubah variable atau mensetting variable


class Hero:
    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
    
    # getter
    
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    
    def diserang(self,serangPower):
        self.__health -= serangPower
    
    
    
# awal dari game
earthShaker = Hero('Earth Shaker',50,5)
print(earthShaker.__dict__)

# game berjalan
 
print(earthShaker.getName())
print(earthShaker.getHealth())

earthShaker.diserang(15)
print(earthShaker.getHealth())