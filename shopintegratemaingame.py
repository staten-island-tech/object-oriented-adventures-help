# Import the shop module and other necessary modules
import shopv2
import random
from monster import Monster
from weapons import weapon
import os 
# Inventory
inventory = []

# Function for loot
def loot():
    loot = random.randint(1, 50)
    if loot in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 41, 42, 43]:
        print("You've found a Ray Gun:", Ray_gun)
    elif loot in [15, 16, 17, 18, 19, 20, 21, 22, 44, 49, 40]:
        print("You've found a Fire Sword:", Fire_sword)
    elif loot in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48]:
        print("You've found a Grenade:", Grenade)
    elif loot == 50:
        print("You've found The Power of the Sun:", The_power_of_the_sun)

# Function for random encounter
def random_number():
    random_number = random.randint(1, 31)
    if random_number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("Nothing")
    elif random_number in [14, 15, 11, 12]:
        print("Found loot")
        loot()
    elif random_number in [16, 20, 13]:
        print(Slime)
    elif random_number in [17, 21]:
        print(Blaze)
    elif random_number in [18, 22]:
        print(Helios)
    elif random_number in [19, 23]:
        print(Octo)

# Monster Definitions
Slime = "[Slime] HP:(30) ATK:(5)"
Blaze = "[Blaze] HP:(65) ATK:(15)"
Helios = "[Helios] HP:(60) ATK:(15)"
Octo = "[Octo] HP:(45) ATK:(12)"

# Additional Monster Definitions
Flaker = Monster(name="Flaker", hp=72, hp_max=72, dmg=17)
Leviathon = Monster(name="Leviathon", hp=105, hp_max=105, dmg=26)

# Weapon Definitions
Fists = weapon(name="Fists", weapon_type="blunt", damage=3, value=0)
Fire_sword = weapon(name="Fire Sword", weapon_type="sharp", damage=22, value=10)
Ray_gun = weapon(name="Ray Gun", weapon_type="ranged", damage=14, value=15)
Grenade = weapon(name="Grenade", weapon_type="ranged", damage=6, value=2)
The_power_of_the_sun = weapon(name="The Power of the Sun", weapon_type="???", damage=1000000000, value=100)

# NPC interaction
def npc():
    person = random.randint(0, 10)
    if person in [1, 5, 6]:
        print("Bobby: Hello there!")
    elif person in [2, 3, 7]:
        print("Jamil: I hate Thursdays...")
    elif person in [4, 8, 9]:
        print("Michael: Hola! Como Estas?")
    elif person == 10:
        print("Dr. Octavious: The power of the sun, in the palm of my hands.")

# Shop interaction
def shop_option(shop, player):
    while True:
        question = input("What do you want to do right now: open shop(1), fight enemy(2), run, move (w, a, s, d): ").lower()
        if question == '1':
            shop.display_items()
            print(f"\n{player.name}'s money: ${player.money}")
            print("Enter the number of the item you want to buy or '0' to exit:")
            
            try:
                choice = int(input("Your choice: "))
                if choice == 0:
                    break
                shop.purchase_item(choice, player)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif question in ['2', 'run', 'w', 'a', 's', 'd']:
            break
        else:
            print("Invalid option, please try again.")

# Game setup
User = input("Please enter a username: ")
print(f"Welcome {User} (your data will not be saved)")
click = input("")
if click == "":
    input("Throughout the game you can collect many chests and fight various monsters. Press Enter to continue...")
    input("Chests will contain weapons of various rarities depending on your luck. Press Enter to continue...")
    input("Use these weapons to fight monsters. Press Enter to continue...")
    input("Lastly, have fun! (probably won't). Press Enter to start the game...")

# Create shop and items
shop = shopv2.Shop()
shop.add_item(shopv2.Item("Sword", 50))
shop.add_item(shopv2.Item("Shield", 30))
shop.add_item(shopv2.Item("Potion", 10))
shop.add_item(shopv2.Item("M16A3", 70))
shop.add_item(shopv2.Item("Ray_Gun", 15))
shop.add_item(shopv2.Item("Grenade", 5))
shop.add_item(shopv2.Item("The Power of the Sun", 1000))

# Create player
player = shopv2.Player(User, 100)

# Game loop
while True:
    direction = input("Move (W/A/S/D): ").lower()
    if direction in ["w", "a", "s", "d"]:
        if direction == "w":
            print(f"Moving Up")
        elif direction == "a":
            print(f"Moving Left")
        elif direction == "s":
            print(f"Moving Down")
        elif direction == "d":
            print(f"Moving Right")
        
        random_number()
        loot()
        shop_option(shop, player)
    else:
        print("Invalid direction. Please choose W, A, S, or D.")
