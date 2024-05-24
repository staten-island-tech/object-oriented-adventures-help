Shockwave = "[Ability]:Energy Field || [Damage]:+3:"
Magman = "[Ability]:Lava Spray || [Damage]:+2.5:"
Hydro = "[Ability]:Water Pump || [Damage]:+3:"
OcTitan = "[Ability]:SUN || [Damage]:+65:"

Select = input("Select a suit (Shockwave/Magman/Hydro): ").lower()
if Select == "123":
    print("OcTitan Suit selected")
    print(OcTitan)
elif Select == "magman":
    print("Magman Suit selected")
    print(Magman)
elif Select == "hydro":
    print("Hydro Suit selected")
    print(Hydro) 
elif Select == "shockwave":
    print(Shockwave)

""" class suits():
    def __init__(self, name: str, ability: int, dmg: int):
        self.name = name
        self.ability = ability
        self.dmg = dmg """



class suits:
    def __init__(self, name: str, defense: int, damage: int, value: int) -> None:
        self.name = name 
        self.defense = defense
        self.damage = damage
        self.value = value 

shockwave = suits(name="shockwave", 
               defense="sharp", 
               damage=4, 
               value=10