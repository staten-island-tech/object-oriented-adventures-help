Slime=0.2
Blaze=0.3
Helios =0.3
Octo =0.5
Flaker =0.9
Leviathon =1.0
startXP = 0

for i in range(3):
    attk = input("Test: ")
    if attk == "s":
        startXP += Slime
        print(startXP)
    elif attk == "b":
        startXP += Blaze
        print(startXP)
    elif attk == "h":
        startXP += Helios
        print(startXP)
    elif attk == "o":
        startXP += Octo
        print(startXP)
    elif attk == "f":
        startXP += Flaker
        print(startXP)
    elif attk == "l":
        startXP += Leviathon
        print(startXP)
print(f"Level:{startXP}")