from weapons import fists        
from weapons import *
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name 
        self.health = health
        self.health_max = health
        
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)



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
                 health: int,
                 weapon: str,
                 ) -> None:
        super().__init__(name=name, health=health)
  

Caseoh = Enemy(name = "Gary Zhou", health = 500, weapon = Fire_sword )
Archer = Enemy(name = "Archer", health = 30, weapon = Recurve_Bow)
Dark_Mage = Enemy(name = "Dark Mage", health = 20, weapon = Staff_of_The_Abyss)
Abyss_Knight = Enemy(name = "Abyss Knight", health= 50, weapon = Iron_sword)
Brute =  Enemy(name = "Brute", health= 80, weapon = Iron_sword)
Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200, Weapon = fists)
Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300, weapon = Grenade )







       


