import random
from player import Hero 
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
            Hero.equip (wooden_sword)

    if loot in [201,350]:
        print(Gernade)
        if self.weapon == fists:
            elif self.weapon == wooden_sword:
            Hero.equip (Gernade)

    if loot in [351,450]:
        print(Ray_gun)
        if self.weapon == fists:
        elif self.weapon == wooden_sword:
        elif self.weapon == Gernade:
             Hero.equip (Ray_gun)

    if loot in [451,499]:
        print(Fire_sword)
        if self.weapon == fists:
        elif self.weapon == wooden_sword:
        elif self.weapon == Gernade:
        elif self.weapon == Ray_gun:
             Hero.equip (Fire_sword)     
        
    if loot in [500]:
        print(The_power_of_the_sun)
        if self.weapon == fists:
        elif self.weapon == wooden_sword:
        elif self.weapon == Gernade:
        elif self.weapon == Ray_gun:
        elif self.weapon == Fire_sword:
            Hero.equip (The_power_of_the_sun)

loot()