import math
from Main_game import Slime, Blaze, Helios, Octo
from weapons import Fists, Ray_gun, Fire_sword, Gernade

""" level = []
Slime=0.2
Blaze=0.3
for i in range(24):
    attk = input("Test: ")
    if attk == "s":
        level.append(Slime)
    elif attk == "b":
        level.append(Blaze)
    
    for Slime in level:
        print(Slime) """


hero = Hero(name="hero", health=100, exp=0)
hero.equip(Ray_gun)
enemy = Enemy(name="enemy", health=30, weapon=Fire_sword)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")
    input()