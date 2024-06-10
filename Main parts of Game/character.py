class Character:
    def __init__(self, name, hp, attack, gold):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.gold = gold

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

