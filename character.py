class Character:
    def _init_(self, name: str, health: int, damage: int):
        self.name = name 
        self.health = health
        self.health_max = health
        self.damage = damage 

    def attack(self, target) -> None:
        target.hp - self.damage
        target.hp = max(target.health, 0)



