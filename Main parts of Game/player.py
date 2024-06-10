from character import Character

<<<<<<< HEAD
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
=======
class Player(Character):
    def __init__(self, name, hp, attack, gold):
        super().__init__(name, hp, attack, gold)
        self.inventory = []
>>>>>>> ed1e4824cb1edce95c4eab456f6f147865e8922e

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage!")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} found {amount} gold! Total gold: {self.gold}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} adds {item.name} to the inventory.")

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(f"- {item.name} (Damage: {item.damage}, Value: {item.value})")
