#Beginning
print("Hello Player!")
User = input("Please enter a username: ")
print(f"Welcome {User}")
click = input("")
if click == "":
    Weapon = input("Select a weapon (Obliterater Gun/Master Sword/Crystal Heart/Telekenises Remote): ")

click = input("Directions: This is an action-adventure game where you'll be able to travese a tiny world and fight bosses ")
click = input("The amount of damage you do will be based off of your answers (Try to be creative) ")
click = input("Interact with characters throughout the map to progress the story ")
click = input("Lastly, have fun! (probably won't) ")

#Movement
Direction = input("Forward/Backward/Lef/Right: ")
if Direction == "Left" or "left":
    print(f"Moving {Direction}")
elif Direction == "Right" or "right":
    print(f"Moving {Direction}")
elif Direction == "Forward" or "forward":
    print(f"Moving {Direction}")
elif Direction == "Backward" or "backward":
    print(f"Moving {Direction}")

#NPCs
print("You've stumbled across [Michael]")
npc = input("Press (E) to interact: ")
if npc == "e":
    click = input("[Michael]: Hello there! I'm tired and don't have enough energy to talk to you. ")
    print("GO AWAY!")

#Tutorial
click = input("You've just interacted with your first NPC ")
click = input("NPCs will be scattered throughout the map ")
click = input("You'll be able to interact with them but they won't help much ")
