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

class Character:
    def __init__(self, name: str, health: int, exp: int) -> None:
        self.name = name 
        self.health = health
        self.health_max = health
        self.exp = exp
        
        self.weapon = Fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")
        
class Hero(Character):
    def __init__(self, name: str, health: int, exp: int) -> None:
        super().__init__(name=name, health=health, exp=exp)

        self.default_weapon = self.weapon

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")
    
    def drop(self, weapon) -> None:
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon

hero = Hero(name="hero", health=100, exp=0)
hero.equip(Ray_gun)
enemy = Enemy(name="enemy", health=30, weapon=Fire_sword)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}: {hero.exp}")
    print(f"health of {enemy.name}: {enemy.health}")
    input()