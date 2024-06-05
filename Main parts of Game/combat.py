import math
from player import Hero, Enemy
from weapons import *

Death = Enemy(name = "Death", health = 500 ) #Fire Sword
Archer = Enemy(name = "Archer", health = 30) #Recurve_Bow
Dark_Mage = Enemy(name = "Dark Mage", health = 20) #Staff of the abyss
Abyss_Knight = Enemy(name = "Abyss Knight", health= 50) #iron sword 
Brute =  Enemy(name = "Brute", health= 80)
Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200, weapon = fists)
Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300, weapon = Grenade )



hero = Hero(name="hero", health=100)
hero.equip(Ray_gun)
enemy = Dark_Mage
enemy.equip(Staff_of_The_Abyss)
while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")
    input()

