class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name 
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value 



fists = weapon(name="Fists", 
               weapon_type="blunt", 
               damage=2, 
               value=0)

wooden_sword = weapon(name="wooden_sword", 
               weapon_type="sharp", 
               damage=4, 
               value=10)

Ray_gun = weapon(name="ray_gun", 
               weapon_type="ranged", 
               damage=10, 
               value=15)





