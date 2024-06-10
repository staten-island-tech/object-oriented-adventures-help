# character.py
from weapons import *
class Character:
    def __init__(self, name: str, health: int, gold: int) -> None:
        self.name = name 
        self.health = health
        self.health_max = health
        self.gold = gold
        
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        if target.health == 0:
            
            
            
            
            
            class Hero(Character):
                def __init__(self,
                    name: str,
                    health: int) -> None:
                        super().__init__(name=name, health=health)
            

        self.default_weapon = self.weapon

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")
    
    def drop(self, weapon) -> None:
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon



class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int
        
                 ) -> None:
        super().__init__(name=name, health=health)


        self.default_weapon = self.weapon
        

    def equi(self, weapon) -> None:
        self.weapon = weapon
       

Death = Enemy(name = "Death", health = 500 ) #Fire Sword
Death.equi(Fire_sword)

Archer = Enemy(name = "Archer", health = 30) #Recurve_Bow
Archer.equi(Recurve_Bow)

Dark_Mage = Enemy(name = "Dark Mage", health = 20) #Staff of the abyss
Dark_Mage.equi(Staff_of_The_Abyss)

Abyss_Knight = Enemy(name = "Abyss Knight", health= 50) #iron sword 
Abyss_Knight.equi(Iron_sword)

Brute =  Enemy(name = "Brute", health= 80) #iron sword
Brute.equi(Iron_sword)

Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200)#fists
Gorlock_the_Destroyer.equi(fists)

Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300 )#grenade
Skibidi_Rizzler.equi(Grenade)
