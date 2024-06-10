from character import Character

class Player(Character):
    def __init__(self, name, hp, attack, gold):
        super().__init__(name, hp, attack, gold)
        self.inventory = []

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