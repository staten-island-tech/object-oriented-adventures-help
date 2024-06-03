import random
from character import Hero, Enemy
from weapon import wooden_sword, Ray_gun

#Random
hero = Hero(name="hero", health=100)

enemy = Enemy(name="enemy", health=30, weapon=wooden_sword)

def fight():
    
        hero.attack(enemy)
        enemy.attack(hero)

        print(f"health of {hero.name}: {hero.health}")
        print(f"health of {enemy.name}: {enemy.health}")
    
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
        
    elif Direction == "Right" or "right":
        print(f"Moving {Direction}")
     
    elif Direction == "Forward" or "forward":
        print(f"Moving {Direction}")

    elif Direction == "Backward" or "backward":
        print(f"Moving {Direction}")
