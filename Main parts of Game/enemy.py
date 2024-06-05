# enemy.py

from character import Character

class Enemy(Character):
    def __init__(self, name, hp, attack, gold):
        super().__init__(name, hp, attack)
        self.gold = gold
