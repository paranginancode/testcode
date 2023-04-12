class Hero: # Templating
    # Class variable
    jumlah = 0 # Jumlah adalah Variable Milik CLass Hero
    
    def __init__(self, inputName, inputHealth, inputPower,inputArmor):
       # Instance Variable, artinya variable akan dimiliki oleh hero1,hero2 dan hero3
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        self.armor = inputArmor
        # Self memiliki level yang sertara dengan hero1,hero2,hero3 
        Hero.jumlah += 1
        print('Membuat hero dengan nama : '+ inputName)
        
        
        
hero1 = Hero('sniper', 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero('mirana', 100, 14, 1)
print(Hero.jumlah)
hero3 = Hero('ucup', 1000, 100, 0)
print(Hero.jumlah)

