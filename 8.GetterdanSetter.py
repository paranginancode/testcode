class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.__health = health
        self.__attackPower = attackPower
        self.__armorNumber = armorNumber
        # self.info = "name {} : \n\thealth: {} \n\tattack: {} \n\tarmor: {}".format(self.name, self.__health, self.__attackPower, self.__armorNumber)
        
        
    @property
    def info(self):
        return "name {} : \n\thealth: {} \n\tattack: {} \n\tarmor: {}".format(self.name, self.__health, self.__attackPower, self.__armorNumber)

    @property
    def armor(self):
        pass
    @armor.getter
    def armor(self):
        return self.__armorNumber
    
    @armor.setter
    def armor(self):
        self.__armorNumber = input
 


sniper = Hero("sniper", 100, 10, 4)
print(sniper.info)
sniper.armorNumber = 50
print(sniper.armorNumber)