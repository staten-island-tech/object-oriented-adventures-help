import random

#Random
def Random():
    random_number = random.randint(1,25)
    if random_number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        print("Nothing")
    if random_number in [16,20]:
        print(Slime)
    if random_number in [17,21]:
        print(Blaze)
    if random_number in [18,22]:
        print(Helios)
    if random_number in [19,23]:
        print(Octo)
    if random_number in [24,25]:
        print("Chest")

Slime = "[Slime] HP:(30) ATK:(5)"
Blaze = "[Blaze] HP:(65) ATK:(15)"
Helios = "[Helios] HP:(60) ATK:(15)"
Octo = "[Octo] HP:(45} ATK:(12)"

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
