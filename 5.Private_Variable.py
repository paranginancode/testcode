class Hero:
    
    # class variable
    jumlah = 0
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
        # Variable Instance Private
        self.__private = "private"
        # Variable Instance Protected
        
        self._protected = "protected"
        
lina = Hero('Lina',100)

