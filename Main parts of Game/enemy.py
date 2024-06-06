# enemy.py

from character import Character

class Enemy(Character):
    def __init__(self, name, hp, attack, gold):
        super().__init__(name, hp, attack)
        self.gold = gold

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack}, Gold: {self.gold})"

# Define some specific enemies
class Slime(Enemy):
    def __init__(self):
        super().__init__(name="Slime", hp=30, attack=5, gold=10)

class Blaze(Enemy):
    def __init__(self):
        super().__init__(name="Blaze", hp=65, attack=15, gold=20)

class Helios(Enemy):
    def __init__(self):
        super().__init__(name="Helios", hp=60, attack=15, gold=25)

class Octo(Enemy):
    def __init__(self):
        super().__init__(name="Octo", hp=45, attack=12, gold=15)

class Flaker(Enemy):
    def __init__(self):
        super().__init__(name="Flaker", hp=72, attack=17, gold=30)

class Leviathon(Enemy):
    def __init__(self):
        super().__init__(name="Leviathon", hp=105, attack=26, gold=50)
