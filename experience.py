import math
Slime=0.2
Blaze=0.3
startXP = 0
level = []

for i in range(3):
    attk = input("Test: ")
    if attk == "s":
        print(startXP + Slime)
        level.append(attk)
    elif attk == "b":
        print(startXP + Blaze)
        level.append(attk)
