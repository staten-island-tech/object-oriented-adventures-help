class suits():
    def __init__(self, name: str, ability: int, dmg: int):
        self.name = name
        self.ability = ability
        self.dmg = dmg

Shockwave = "[Ability]:Energy Field || [Damage]:+3:"
Magman = "[Ability]:Lava Spray || [Damage]:+2.5:"
Hydro = "[Ability]:Water Pump || [Damage]:+3:"
OcTitan = "[Ability]:SUN || [Damage]:+65:"

Select = input("Select a suit (Shockwave/Magman/Hydro): ")
if Select == "643":
    print("OcTitan Suit selected")
    print(OcTitan)
elif Select == "Magman" or "magman":
    print(f"{Select} Suit selected")
elif Select == "hydro":
    print(f"{Select} Suit selected")