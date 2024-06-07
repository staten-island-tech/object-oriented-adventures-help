from character import Character

class Enemy(Character):
    def __init__(self, name, hp, attack, gold):
        super().__init__(name, hp, attack, gold)

class Slime(Enemy):
    def __init__(self):
        super().__init__("Slime", 30, 5, 10)

class Blaze(Enemy):
    def __init__(self):
        super().__init__("Blaze", 65, 15, 20)

class Helios(Enemy):
    def __init__(self):
        super().__init__("Helios", 60, 15, 25)

class Octo(Enemy):
    def __init__(self):
        super().__init__("Octo", 45, 12, 15)

class Flaker(Enemy):
    def __init__(self):
        super().__init__("Flaker", 72, 17, 30)

class Leviathon(Enemy):
    def __init__(self):
        super().__init__("Leviathon", 105, 26, 50)
