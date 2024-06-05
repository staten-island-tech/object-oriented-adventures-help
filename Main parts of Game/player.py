import os     
from weapons import fists, wooden_sword , Fire_sword, Ray_gun, Grenade

# player.py

class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.money = 100
        self.inventory = []

    def attack_enemy(self, enemy):
        enemy.hp -= self.attack
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage. {enemy.name} HP: {enemy.hp}")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage. HP: {self.hp}")

    def add_gold(self, amount):
        self.money += amount
        print(f"{self.name} received {amount} gold. Total gold: {self.money}")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory.")

    def show_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}")

class enemy:
    def __init__(self , mob_name , mob_hp , mob_atk, mob_defense):
        self.name = mob_name
        self.hp = mob_hp
        self.atk = mob_atk
        self.defense = mob_defense
       


    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
""" 

Gary_Zhou = playable_character(name = "Gary Zhou", characters_hp = 500, characters_atk = 20 , characters_defense = 5)
Archer = playable_character(name = "Archer", characters_hp = 30, characters_atk = 30, characters_defense= 0 )
Wizard = playable_character(name = "Wizard", characters_hp = 20, characters_atk= 35, characters_defense= 0)
Knight = playable_character(name = "Knight", characters_hp= 50, characters_atk= 12, characters_defense= 2 )
Brute =  playable_character(name = "Brute", characters_hp= 80, characters_atk= 10 , characters_defense=4 )
Gorlock_the_Destroyer = playable_character(name = "Gorlock the Destroyer", characters_hp=200, characters_atk= 1)
Skibidi_Rizzler = playable_character(name = "Skibidi Rizzler", characters_hp=300, characters_atk=5, characters_defense=3) """



