import random

#Random
def Random():
    random_number = random.randint(1,25)
    if random_number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
        print("Nothing")
    if random_number in [18,19,20,21,22,23]:
        print(slime)
    if random_number in [24,25]:
        print("Chest")

    Slime = 3
    Mhp = 30
    Matk = 5
    Slime.append({"Shp":Mhp, "Satk":Matk})

    Blaze = []
    Mhp = 65
    Matk = 15
    Blaze.append({"Bhp":Mhp, "Batk":Matk})

    Helios = []
    Mhp = 60
    Matk = 15
    Helios.append({"Hhp":Mhp, "Hatk":Matk})

    Octo = []
    Mhp = 45
    Matk = 12
    Octo.append({"Ohp":Mhp, "Oatk":Mhp})

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
