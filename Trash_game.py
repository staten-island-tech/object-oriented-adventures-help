

import random

#Random
inventory = []

def chest():
    chest = random.randint(1,50)
    if chest in [1,5,10,11,15,20,21,25,30,31,35,40,]:
        print("You've found a chest!!!")
        open_chest = input("Press E to open")
        if input= "e" 

def loot():
    loot = random.randint(1,100)
    if loot in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
        print(Ray_gun)
        inventory.append
    if loot in [15,16,17,18,19,20,21,22]:
        print(Fire_sword)
        inventory.append
    if loot in [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]:
        print(Grenade)
        inventory.append    
    if loot in [40]:
        print(The_power_of_the_sun)
        inventory.append
    if loot in [99,66,55,77]:
        print("You found nothing, get scammed.")

def chest():
    chest = random.randint(1,200)
    if chest in [1,50,5,20,200,10,30]:
        print("You've found a chest!")
    open_chest = input("Press (E) to open the chest")
    if open_chest == "e" or "E":
        loot()

def Random():
    random_number = random.randint(1,23)
    if random_number in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
        print("Nothing")
    if random_number in [14,15]:
        print("found loot")
        loot() 
    if random_number in [16,20]:
        print(Slime)
    if random_number in [17,21]:
        print(Blaze)
    if random_number in [18,22]:
        print(Helios)
    if random_number in [19,23]:
        print(Octo)


Slime = "[Slime] HP:(30) ATK:(5)"
Blaze = "[Blaze] HP:(65) ATK:(15)"
Helios = "[Helios] HP:(60) ATK:(15)"
Octo = "[Octo] HP:(45} ATK:(12)"
    



Ray_gun = "[Ray Gun] DMG:(8)"
Fire_sword = "[Fire Sword] DMG:(12)"
Grenade = "[Gernade] DMG:(4)"
The_power_of_the_sun = "[The Power of the Sun] DMG:(10000000000000)"

User = input("Please enter a username: ") 
print(f"Welcome {User}")
click = input("")
if click == "":
    click = input("Throughout the game you can collect many chests and fight various monsters ")
    click = input("Chests will contain weapons of various rarities depending on your luck ")
    click = input("Use these weapons to fight monsters ")   
    click = input("Lastly, have fun! (you probably won't) ")

for i in range(24973932195):
    Direction = input("Forward/Backward/Left/Right: ")
    direction = Direction.upper()
    if Direction == "Left" or "left":
        print(f"Moving {Direction}")
        Random()

    elif Direction == "Right" or "right":
        print(f"Moving {Direction}")
        Random()
    
    elif Direction == "Forward" or "forward":
        print(f"Moving {Direction}")
        Random()

        
    elif Direction == "Backward" or "backward":
        print(f"Moving {Direction}")
        Random()

        inventory.append(loot)
        print(inventory)
