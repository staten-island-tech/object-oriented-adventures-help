class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name 
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value 

Fists = weapon(name="Fists", 
    weapon_type="blunt", 
    damage=3, 
    value=0)

wooden_sword = weapon(name="wooden_sword", 
               weapon_type="sharp", 
               damage=4, 
               value=5)

Fire_sword = weapon(name="Fire Sword", 
    weapon_type="sharp", 
    damage=22, 
    value=10)

Ray_gun = weapon(name="Ray Gun", 
    weapon_type="ranged", 
    damage=14, 
    value=15)

Gernade = weapon(name="Gernade",
    weapon_type="ranged projectile",
    damage=6,
    value=2)

The_power_of_the_sun = weapon(name="The Power of the Sun",
    weapon_type="???",
    damage=1000000000,
    value=1000)
