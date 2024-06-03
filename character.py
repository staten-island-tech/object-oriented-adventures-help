from weapons import *
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name 
        self.health = health
        self.health_max = health
        
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)



class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int) -> None:
        super().__init__(name=name, health=health)
    

        self.default_weapon = self.weapon

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")
    
    def drop(self, weapon) -> None:
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.default_weapon



class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int
        
                 ) -> None:
        super().__init__(name=name, health=health)


        self.default_weapon = self.weapon
        

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")