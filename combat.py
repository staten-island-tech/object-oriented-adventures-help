import math
from character import Hero, Enemy
from weapons import *

Caseoh = Enemy(name = "Gary Zhou", health = 500, weapon = Fire_sword )
Archer = Enemy(name = "Archer", health = 30, weapon = Recurve_Bow)
Dark_Mage = Enemy(name = "Dark Mage", health = 20, weapon = Staff_of_The_Abyss)
Abyss_Knight = Enemy(name = "Abyss Knight", health= 50, weapon = Iron_sword)
Brute =  Enemy(name = "Brute", health= 80, weapon = Iron_sword)
Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200, Weapon = fists)
Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300, weapon = Grenade )


hero = Hero(name="hero", health=100)
hero.equip(Ray_gun)
enemy = Enemy(name="enemy", health=30, weapon=wooden_sword)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")
    input()

