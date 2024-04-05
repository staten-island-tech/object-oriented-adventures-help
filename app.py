#Beginning
print("Hello Player!")
User = input("Please enter a username: ")
difficulty = input("Select a difficulty level (Baby mode/Average human/Super human): ")
Weapon = input("Select a secondary weapon (Ray gun/Time bomb/Healing stone/Mind bug): ")
print("Directions: This is an action-adventure game where you'll be able to travese a tiny world and fight bosses.")
print("The amount of damage you do will be based off of your answers (Try to be creative).")
print("Interact with characters throughout the map to progress the story.")
print("Have fun! (probably won't)")

#Movement
Direction = input("Forward/Backward/Lef/Right:  ")
if Direction == "Left" or "left":
    print(f"Moving {Direction}")
elif Direction == "Right" or "right":
    print(f"Moving {Direction}")
elif Direction == "Forward" or "forward":
    print(f"Moving {Direction}")
elif Direction == "Backward" or "backward":
    print(f"Moving {Direction}")

#NPCs
print("You've stumbled across [NPC]")
npc = input("Press (E) to interact: ")
if npc == "e":
    print("[NPC]: Hello there! I'm tired and don't have enough energy to talk to you.")

