class Monster():
    def __init__(self, name: str, hp: int, hp_max: int, dmg: int, exp: int):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.dmg = dmg
        self.exp = exp

    def attack(self, target):
        dmg_done = target.hp - self.dmg
        target.hp = max(target.hp, 0)


