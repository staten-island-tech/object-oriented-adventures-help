import random

#Random
inventory = []
def loot():
    loot = random.randint(1,40)
    if loot in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
        print(Ray_gun)
        inventory.append
    if loot in [15,16,17,18,19,20,21,22]:
        print(Fire_sword)
        inventory.append
    if loot in [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]:
        print(Gernade)
        inventory.append
    if loot in [40]:
        print(The_power_of_the_sun)
        inventory.append

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

<<<<<<< HEAD

=======
def loot():
    loot = random.randint(0,100)
    if loot in [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99]:
        print("You've found a", Ray_gun)
    if loot in [10,20,30,40,50,60,70,80,90,100,15,20,25,30,65]:
        print("You've found",Fire_sword)
    if loot in [2,3,5,7,11,13,17,19,23,29,31,34,37,]:
        print("You found a grenade",Gernade)
    if loot in [1,100]:
        print("You've found", The_power_of_the_sun)
>>>>>>> 680748d2e4762e76b94f51acfb455139cd58e8b7

Ray_gun = "[Ray Gun] DMG:(8)"
Fire_sword = "[Fire Sword] DMG:(12)"
Gernade = "[Gernade] DMG:(3)"
The_power_of_the_sun = "[The Power of the Sun] DMG:(10000000000000)"

User = input("Please enter a username: ") 
print(f"Welcome {User}")
click = input("")
if click == "":
    click = input("Throughout the game you can collect many chests and fight various monsters ")
    click = input("Chests will contain weapons of various rarities depending on your luck ")
    click = input("Use these weapons to fight monsters ")
    click = input("Lastly, have fun! (probably won't) ")

for i in range(24973932195):
    Direction = input("Forward/Backward/Left/Right: ")
    direction = Direction.upper()
    if Direction == "Left" or "left":
        print(f"Moving {Direction}")
        Random()
        loot()
    elif Direction == "Right" or "right":
        print(f"Moving {Direction}")
        Random()
        loot()
    elif Direction == "Forward" or "forward":
        print(f"Moving {Direction}")
        Random()
        loot()
    elif Direction == "Backward" or "backward":
        print(f"Moving {Direction}")
        Random()
        loot()
 