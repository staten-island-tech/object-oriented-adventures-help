from weapon import wooden_sword



class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name 
        self.health = health
        self.health_max = health
        
        self.weapon = wooden_sword

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        
        

