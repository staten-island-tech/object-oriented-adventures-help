Caseoh = Enemy(name = "Gary Zhou", health = 500, weapon = Fire_sword )
Archer = Enemy(name = "Archer", health = 30, weapon = Recurve_Bow)
Dark_Mage = Enemy(name = "Dark Mage", health = 20, weapon = Staff_of_The_Abyss)
Abyss_Knight = Enemy(name = "Abyss Knight", health= 50, weapon = Iron_sword)
Brute =  Enemy(name = "Brute", health= 80, weapon = Iron_sword)
Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200, Weapon = fists)
Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300, weapon = Grenade )


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
    

