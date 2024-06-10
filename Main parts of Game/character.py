class Character:
<<<<<<< HEAD
    def __init__(self, name: str, health: int, gold: int) -> None:
        self.name = name 
        self.health = health
        self.health_max = health
        self.gold = gold
        
        self.weapon = fists
=======
    def __init__(self, name, hp, attack, gold):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.gold = gold
>>>>>>> ed1e4824cb1edce95c4eab456f6f147865e8922e

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, Attack: {self.attack})"

<<<<<<< HEAD

class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int
        
                 ) -> None:
        super().__init__(name=name, health=health)


        self.default_weapon = self.weapon
        

    def equi(self, weapon) -> None:
        self.weapon = weapon
       

Death = Enemy(name = "Death", health = 500 ) #Fire Sword
Death.equi(Fire_sword)

Archer = Enemy(name = "Archer", health = 30) #Recurve_Bow
Archer.equi(Recurve_Bow)

Dark_Mage = Enemy(name = "Dark Mage", health = 20) #Staff of the abyss
Dark_Mage.equi(Staff_of_The_Abyss)

Abyss_Knight = Enemy(name = "Abyss Knight", health= 50) #iron sword 
Abyss_Knight.equi(Iron_sword)

Brute =  Enemy(name = "Brute", health= 80) #iron sword
Brute.equi(Iron_sword)

Gorlock_the_Destroyer = Enemy(name = "Gorlock the Destroyer", health=200)#fists
Gorlock_the_Destroyer.equi(fists)

Skibidi_Rizzler = Enemy(name = "Skibidi Rizzler", health=300 )#grenade
Skibidi_Rizzler.equi(Grenade)
=======
>>>>>>> ed1e4824cb1edce95c4eab456f6f147865e8922e
