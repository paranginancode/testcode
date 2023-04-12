# OOP adalah salah satu bagian dari paradigma pemrograman yang berfokus pada objek.
# Selain OOP ada paradigma lain seperti Procedural Programming dan Functional Programming.


# Contoh Code Paradigma Prosedural 

class Hero:
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = 'okto'
hero1.health = 1000
hero2.name = 'capung'
hero2.health = 500
hero3.name = 'bokis'
hero3.health = 250

print(hero1.__dict__)
print(hero1)
print(hero1.name)

## Program diatas dapat disederhanakan dengan menggunakan OOP menjadi kode sebagai berikut:

class Hero:
    def __init__(self, inputName, inputHealth):
        self.name = inputName
        self.health = inputHealth

hero1 = Hero('okto', 1000)
hero2 = Hero('capung', 500)

print(hero1.Hero())
print(hero2)

