import math
from character import Hero, Enemy
from weapons import *

Death = Enemy(name = "Death", health = 500 ) #Fire Sword
Death.equip(Fire_sword)

Archer = Enemy(name = "Archer", health = 30) #Recurve_Bow
Archer.equip(Recurve_Bow)

Dark_Mage = Enemy(name = "Dark Mage", health = 20) #Staff of the abyss
Dark_Mage.equip(Staff_of_The_Abyss)

Abyss_Knight = Enemy(name = "Abyss Knight", health= 50) #iron sword 
Abyss_Knight.equip(Iron_sword)

Brute =  Enemy(name = "Brute", health= 80) #iron sword
Brute.equip(Iron_sword)

Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200)#fists
Gorlock_the_Destroyer.equip(fists)

Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300 )#grenade
Skibidi_Rizzler.equip(Grenade)


hero = Hero(name="hero", health=100)
hero.equip(Ray_gun)
enemy = Gorlock_the_Destroyer

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")
    input()

