class suits():
    def __init__(self, name: str, ability: int, dmg: int):
        self.name = name
        self.ability = ability
        self.dmg = dmg

Shockwave = suits(name = "Shockwave Suit",ability = "Energy Field",dmg = +3)
Magman = suits(name = "Magman Suit",ability = "Lava Spray",dmg = +2.5)
Hydro = suits(name = "Hydro Suit",ability = "Water Pump",dmg = +3)
OcTitan = suits(name = "OcTitan Suit",ability = "Sun",dmg = +65)

Select = input("Select a suit (Shockwave/Magman/Hydro): ")
if Select == "643":
    print("OcTitan Suit selected")
if Select == "Hydro" or "hydro":
    print(f"{Select} Suit selected")