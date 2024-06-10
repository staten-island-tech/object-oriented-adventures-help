# player.py

class Player:
    def __init__(self, name, hp, attack, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.gold = gold

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)

    def add_gold(self, amount):
        self.gold += amount

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack}, Gold: {self.gold})"
