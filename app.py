#Beginning
import time
import sys



User = input("Please enter a username: ")
print(f"Welcome {User}")
click = input("")


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
if click == "":
    Weapon = input("Select a weapon (Obliterator Gun/Master Sword/Crystal Heart/Telekenises Remote):\n ")

delay_print("Directions:")
time.sleep(1)
delay_print(" This is an action-adventure game where you'll be able to travese a tiny world and fight bosses\n")
time.sleep(1)
delay_print("The amount of damage you do will be based off of your answers")
time.sleep(0.5)
delay_print("(Try to be creative)\n")
time.sleep(1)
delay_print("Interact with characters throughout the map to progress the story\n ")
time.sleep(2)
delay_print("Lastly, have fun! (probably won't)\n")


#Movement
Direction = input("Forward/Backward/Left/Right: ")
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
print("Press (E) to interact")
npc = input("Press (X) to ignore: ")
if npc == "e":
    click = input("[Michael]: Hello there! I'm tired and don't have enough energy to talk to you. ")
    delay_print("GO AWAY!")
    time.sleep(0.5)
    delay_print("You've just interacted with your first NPC ")
    time.sleep(0.5)
    delay_print("NPCs will be scattered throughout the map ")
    time.sleep
    delay_print("You'll be able to interact with them but they won't help much ")
else:
    print("You walked past the NPC")
