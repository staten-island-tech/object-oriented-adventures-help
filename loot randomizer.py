import random
from character import Hero 
from weapons import fists, wooden_sword, Ray_gun, Fire_sword, Gernade, The_power_of_the_sun

def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

def drop(self, weapon) -> None:
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon


def loot():
    loot = random.randint(1,500)

    if loot in [1,200]:
        print(wooden_sword)
        if self.weapon == fists:
            

    if loot in [201,350]:
        print(Ray_gun)

    if loot in [351,450]:
        print(Fire_sword)

    if loot in [451,499]:
        print(Gernade)

    if loot in [500]:
        print(The_power_of_the_sun)