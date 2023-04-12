class Hero:
    def __init__(self,inputName,inputPower,inputHealth):
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        
hero1 = Hero('okto', 100, 1000)
hero2 = Hero('capung', 50, 500)
hero3 = Hero('bokis', 25, 250)

print(hero1.__dict__)
print(hero1.name  + ' has power ' + str(hero1.power) + ' and health ' + str(hero1.health))
print(hero2.name + ' has power ' + str(hero2.power) + ' and health ' + str(hero2.health))
print(hero3.name + ' has power ' + str(hero3.power) + ' and health ' + str(hero3.health))