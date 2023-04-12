class Hero:
    __jumlah = 0
    
    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1
        
    # Methode ini hanya berlaku untuk objek dan tidak berlaku unutk class
    
    def getJumlah(self):
        return Hero.__jumlah
    
    # Methode ini hanya berlaku unutk class dan tidak berlaku untuk objek
    
    def getJumlah1():
        return Hero.__jumlah
    
    # Methode Static(Decorator) nempel ke objek dan class
    
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah
    
    # Methode Class(Decorator) nempel ke class
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = Hero('Sniper')
print(Hero.getjumlah2())
rikimaru = Hero('Rikimaru')
drowranger = Hero('Drow Ranger')

print(Hero.getJumlah3())