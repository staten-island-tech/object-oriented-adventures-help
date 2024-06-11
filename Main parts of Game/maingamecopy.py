import random
import time
from player import Player
from enemy import Slime, Blaze, Helios, Octo, Flaker, Leviathon
import shopv2
from weapons import weapon

# Inventory
inventory = []

# Function for loot
def loot():
    loot = random.randint(1, 50)
    if loot in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 41, 42, 43]:
        print("You've found a Ray Gun:", Ray_gun.weapon_type, Ray_gun.damage, Ray_gun.value)
        inventory.append(Ray_gun)
    elif loot in [15, 16, 17, 18, 19, 20, 21, 22, 44, 49, 40]:
        print("You've found a Fire Sword:", Fire_sword.weapon_type, Fire_sword.damage, Fire_sword.value)
        inventory.append(Fire_sword)
    elif loot in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48]:
        print("You've found a Grenade:", Gernade.weapon_type, Gernade.damage, Gernade.value)
        inventory.append(Gernade)
    elif loot == 50:
        print("You've found The Power of the Sun:", The_power_of_the_sun.weapon_type, The_power_of_the_sun.damage, The_power_of_the_sun.value)
        inventory.append(The_power_of_the_sun)

# Weapon Definitions
Fists = weapon(name="Fists", weapon_type="|blunt|", damage=1, value=0)
Fire_sword = weapon(name="Fire Sword", weapon_type="|sharp|", damage=22, value=40)
Ray_gun = weapon(name="Ray Gun", weapon_type="|ranged|", damage=14, value=30)
Gernade = weapon(name="Gernade", weapon_type="|ranged|", damage=6, value=2)
The_power_of_the_sun = weapon(name="The Power of the Sun", weapon_type="|???|", damage=1000000000, value=100)

# Generate a simple math question
def generate_math_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"What is {num1} {operation} {num2}? "
    return question, answer

# Battle function
def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        question, answer = generate_math_question()
        print(f"{player.name} encounters {enemy.name}!")
        try:
            player_answer = int(input(question))
            if player_answer == answer:
                print("Correct! You attack the enemy.")
                player.attack_enemy(enemy)
            else:
                print("Wrong! The enemy attacks you.")
                player.take_damage(enemy.attack)
        except ValueError:
            print("Invalid input! The enemy attacks you.")
            player.take_damage(enemy.attack)
        
        if not enemy.is_alive():
            print(f"You defeated {enemy.name}!")
            player.add_gold(enemy.gold)
        elif not player.is_alive():
            print("You have been defeated!")

# Function for random encounter
def random_number(player):
    random_number = random.randint(1, 50)
    print(f"Random encounter roll: {random_number}")  # Debug statement
    if random_number in range(1, 7):
        print("Nothing happened.")
    elif random_number in range(14, 16) or random_number in range(11, 13):
        print("Found loot!")
        loot()
    elif random_number >= 17:
        enemy = random.choice([Slime(), Blaze(), Helios(), Octo(), Flaker(), Leviathon()])
        print(f"Encountered {enemy.name}!")
        battle(player, enemy)

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
def shop_option(shop, player, inventory ):
    while True:
        question = input("What do you want to do right now: open shop(1), fight enemy(2), run, move (w, a, s, d): ").lower()
        if question == '1':
            shop.display_items()
            print(f"\n{player.name}'s money: ${player.gold} {player.inventory}")
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
    input("Throughout the game you can collect various weapons and fight monsters using them. Press Enter to continue...")
    input("Some monsters might take longer to beat than others but will give you more gold. Press Enter to continue...")
    input("Gold can be used to buy weapons from the shop(still in development). Press Enter to continue...")
    input("To fight the monsters you have to answer a series of math problems. Press Enter to continue...")
    input("Correct answer = Deal damage |Incorrect answer = X_X. Press Enter to continue...")
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
player = Player(User, 150, 15, 0)  # Increased health to 150 and added a healing factor

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
        
        random_number(player)
        player.hp += 1  # Player heals 1 HP after each move
        shop_option(shop, player, inventory)
    else:
        print("Invalid direction. Please choose W, A, S, or D.")
#test