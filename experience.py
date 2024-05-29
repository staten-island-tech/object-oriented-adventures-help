from fuygihoj import Slime, Blaze, Helios, Octo

level = []
Slime=0.2
Blaze=0.3
for i in range(24):
    attk = input("Test: ")
    if attk == "s":
        level.append(Slime)
    elif attk == "b":
        level.append(Blaze)
    
    for Slime in level:
        print(Slime)

