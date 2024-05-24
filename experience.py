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


""" level = []
Slime=0.2
Blaze=0.3
for i in range(24): 
    monster = (input("Test: "))
    if monster == "slime":
        level.append(Slime)
    elif monster == "blaze":
        level.append(Blaze)

level.append(monster)
print("XP:")
for monster in level:
    print(monster)
 """