import math
from player import Hero, Enemy
from weapons_copy import wooden_sword, Ray_gun




hero = Hero(name="hero", health=100)
hero.equip(Ray_gun)
enemy = Enemy(name="enemy", health=30, weapon=wooden_sword)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")
    input()

