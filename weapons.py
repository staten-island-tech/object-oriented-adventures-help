import json
class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name 
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value 

fists = weapon(name="Fists", 
    weapon_type="blunt", 
    damage=1, 
    value=0)

wooden_sword = weapon(name="wooden_sword", 
               weapon_type="sharp", 
               damage=4, 
               value=5)

Iron_sword = weapon(name="Iron Sword", 
               weapon_type="sharp", 
               damage=10, 
               value=10)


Fire_sword = weapon(name="Fire Sword", 
    weapon_type="sharp", 
    damage=22, 
    value=40)

Ray_gun = weapon(name="Ray Gun", 
    weapon_type="ranged", 
    damage=14, 
    value=30)

Recurve_Bow = weapon(name="Recurve Bow", 
    weapon_type="ranged", 
    damage=30, 
    value=60)

Staff_of_The_Abyss = weapon(name="Staff_of_The_Abyss", 
    weapon_type="dark magic", 
    damage=35, 
    value=72)




Grenade = weapon(name="Grenade",
    weapon_type="ranged",
    damage=6,
    value=2)

The_power_of_the_sun = weapon(name="The Power of the Sun",
    weapon_type="???",
    damage=1000000000,
    value=1000000)

with open("weapon.json", "w") as weapon:
    json.dump(Grenade, weapon)
    json.dump(The_power_of_the_sun, weapon)
    json.dump(Staff_of_The_Abyss, weapon)
    json.dump(Recurve_Bow, weapon)
    json.dump(Ray_gun, weapon)
    json.dump(Fire_sword, weapon)
    json.dump(Iron_sword, weapon)
    json.dump(wooden_sword, weapon)
    json.dump(fists, weapon)
    






