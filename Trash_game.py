import random

#Random
def Random():
    random_number = random.randint(1,20)
    if random_number == int(1,2,3,4,5,6,7,8,9,10):
        print("Nothing")
    if random_number == int(11,12,13,14,15,16,17):
        print("Monster")
    if random_number == int(18,19,20):
        print("Chest")
print("Welcome to Trash the game!")

User = input("Please enter a username: ")
print(f"Welcome {User}")
click = input("")
if click == "":
    click = input("Throughout the game you can collect many chests and fight various monsters ")
    click = input("Chests will contain weapons of various rarities depending on your luck ")
    click = input("Use these weapons to fight monsters ")
    click = input("Lastly, have fun! (probably won't) ")

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
