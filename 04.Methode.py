class Hero:
    jumlah_hero = 0
    
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    # Methode tanpa argument/return , tanpa return(void function)
    def siapa(self):
        print('Nama Hero adalah : ' + self.name)
        
    # Methode denan argument
    
    def healthUp(self,up):
        self.health += up
    
    # Methode dengan return
    
    def getHealth(self):
        return self.health   
        
hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 90, 15, 1)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())