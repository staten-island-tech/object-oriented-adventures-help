class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name 
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value 



fists = weapon(name="Fists", weapon_type="blunt", damage=2, value=10)

wooden_sword = weapon(name="wooden_sword" ,weapon_type="sharp" ,damage=4,value=10)

Ray_gun = weapon(name="Ray_Gun",weapon_type="ranged",damage=8 ,value=25)

Fire_sword = weapon(name="Fire_Sword",weapon_type ="close_range",damage = 30,value = 20)

Grenade = weapon(name = "Grenade",weapon_type ="projectile",damage = 10, value = 2)

The_power_of_the_sun= weapon(name = "The Power of the Sun",weapon_type = "god weapon", damage = 10000000000000, value = 100000)

bow = weapon(name= "bow", weapon_type = "long range", damage = "30", value= 3  )
                     

