class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    def serang(self, opponent):
        print(self.name +' menyerang ' + opponent.name)
        opponent.diserang(self, self.attackPower)
    def diserang(self, opponent, opponent_attackPower):
        print(self.name +' diserang ' + opponent.name)
        damage = opponent_attackPower/self.armorNumber
        print('Damage Yang Diterima : ' + str(damage))
        self.health -= damage
        print('Darah ' + self.name + ' tersisa ' + str(self.health))
        
        
        
sniper  = Hero('Sniper', 100, 10, 1)
rikimaru = Hero('Rikimaru', 90, 15, 3)

sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)