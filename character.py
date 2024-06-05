import os     
from weapons import fists, wooden_sword , Fire_sword, Ray_gun, Grenade

class playable_character:
    def __init__(self, characters_name, characters_hp, characters_atk ,characters_defense):
        self.name = characters_name
        self.hp = characters_hp
        self.atk = characters_atk
        self.defense = characters_defense
if playable_character.hp < 0: 
    print("You Died....... bum")
    os.abort()

class enemy:
    def __init__(self , mob_name , mob_hp , mob_atk, mob_defense):
        self.name = mob_name
        self.hp = mob_hp
        self.atk = mob_atk
        self.defense = mob_defense
       


    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)


Gary_Zhou = playable_character(name = "Gary Zhou", characters_hp = 500, characters_atk = 20 , characters_defense = 5)
Archer = playable_character(name = "Archer", characters_hp = 30, characters_atk = 30, characters_defense= 0 )
Wizard = playable_character(name = "Wizard", characters_hp = 20, characters_atk= 35, characters_defense= 0)
Knight = playable_character(name = "Knight", characters_hp= 50, characters_atk= 12, characters_defense= 2 )
Brute =  playable_character(name = "Brute", characters_hp= 80, characters_atk= 10 , characters_defense=4 )
Gorlock_the_Destroyer = playable_character(name = "Gorlock the Destroyer", characters_hp=200, characters_atk= 1)
Skibidi_Rizzler = playable_character(name = "Skibidi Rizzler", characters_hp=300, characters_atk=5, characters_defense=3)




class Enemy(Character):
    def __init__(self,name: str,
                 health: int,
                 weapon,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = wooden_sword
