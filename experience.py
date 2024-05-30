import math
Slime=0.2
Blaze=0.3
level = []

for i in range(3):
    attk = input("Test: ")
    if attk == "s":
        level.append(Slime)
        print(Slime)
    elif attk == "b":
        level.append(Blaze)
        print(Blaze)
