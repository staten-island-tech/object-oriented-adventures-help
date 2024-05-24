import random
from monster import Monster
from weapons import weapon
#Random
inventory = []
def loot():
    loot = random.randint(1,50)
    if loot in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,41,42,43]:
        print(Ray_gun)

    if loot in [15,16,17,18,19,20,21,22,44,49,40]:
        print(Fire_sword)

    if loot in [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,45,46,47,48]:
        print(Gernade)

    if loot in [50]:
        print(The_power_of_the_sun)


def Random():
    random_number = random.randint(1,31)
    if random_number in [1,2,3,4,5,6,7,8,9,10]:
        print("Nothing")
    if random_number in [14,15,11,12]:
        print("Nothing")
    if random_number in [16,20,13]:
        print(Slime)
    if random_number in [17,21]:
        print(Blaze)
    if random_number in [18,22]:
        print(Helios)
    if random_number in [19,23]:
        print(Octo)
    if random_number in [28,29]:
        print(Flaker)
    if random_number in [31,30]:
        print(Leviathon)
    if random_number in [24,25,26,27]:
        print("[npc]")
        npc()

Slime = Monster(name = "Slime", hp = 30, hp_max = 30, dmg = 5, exp = 0.3)
Blaze = Monster(name = "Blaze", hp = 65, hp_max = 65, dmg = 15, exp = 0.4)
Helios = Monster(name = "Helios", hp = 60, hp_max = 60, dmg = 15, exp = 0.4)
Octo = Monster(name = "octo", hp = 45, hp_max = 45, dmg = 12, exp = 0.6)
Flaker = Monster(name = "Flaker", hp = 72, hp_max = 72, dmg = 17, exp = 0.9)
Leviathon = Monster(name = "Leviathon", hp = 105, hp_max = 105, dmg = 26, exp = 1.0)


def loot():
    loot = random.randint(0,100)
    if loot in [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99]:
        print("You've found a",Ray_gun.name, Ray_gun.weapon_type, Ray_gun.damage)
    if loot in [10,20,30,40,50,60,70,80,90,100,15,20,25,30,65]:
        print("You've found a",Fire_sword.name, Fire_sword.weapon_type, Fire_sword.damage)
    if loot in [2,3,5,7,11,13,17,19,23,29,31,34,37,100]:
        print("You found a",Gernade.name, Gernade.weapon_type, Gernade.damage)
    if loot in [1]:
        print("You've found",The_power_of_the_sun.name, The_power_of_the_sun.weapon_type, The_power_of_the_sun.damage)

Fists = weapon(name="Fists", weapon_type="|blunt|", damage=3, value=0)
Fire_sword = weapon(name="Fire Sword", weapon_type="|sharp|", damage=22, value=10)
Ray_gun = weapon(name="Ray Gun", weapon_type="|ranged|", damage=14, value=15)
Gernade = weapon(name="Gernade", weapon_type="|ranged|", damage=6, value=2)
The_power_of_the_sun = weapon(name="The Power of the Sun", weapon_type="|???|", damage=1000000000, value=100)

def npc():
    person = random.randint(0,10)
    if person in [1,5,6]:
        print("Bobby: Hello there!")
    if person in [2,3,7]:
        print("Jamil: I hate Thursdays...")
    if person in [4,8,9]:
        print("Michael: Hola! Como Estas?")
    if person in [10]:
        print("Dr. Octavious: The power of the sun, in the palm of my hands.")

User = input("Please enter a username: ") 
print(f"Welcome {User}")
click = input("")
if click == "":
    click = input("Throughout the game you can collect many weapons which can be used to fight various monsters ")
    click = input("All weapons have a random chance of spawning and deal a certain amount of damage ")
    click = input("Use these weapons to fight monsters ")
    click = input("Lastly, have fun! (probably won't) ")

""" Shockwave = "[Ability]:Energy Field || [Damage]:+3:"
Magman = "[Ability]:Lava Spray || [Damage]:+2.5:"
Hydro = "[Ability]:Water Pump || [Damage]:+3:"
OcTitan = "[Ability]:SUN || [Damage]:+65:"
Select = input("Select a suit (Shockwave/Magman/Hydro): ").lower()
if Select == "123":
    print("OcTitan Suit selected")
    print(OcTitan)
elif Select == "magman":
    print("Magman Suit selected")
    print(Magman)
elif Select == "hydro":
    print("Hydro Suit selected")
    print(Hydro) 
elif Select == "shockwave":
    print(Shockwave) """

for i in range(2497393215):
    Direction = input("Forward/Backward/Left/Right: ")
    direction = Direction.upper()
    if Direction == "Left" or "left":
        print(f"[Moving {Direction}]")
        Random()

    elif Direction == "Right" or "right":
        print(f"[Moving {Direction}]")
        Random()

    elif Direction == "Forward" or "forward":
        print(f"[Moving {Direction}]")
        Random()

    elif Direction == "Backward" or "backward":
        print(f"[Moving {Direction}]")
        Random()

""" Slime = "[Slime] HP:(30) ATK:(5)"
Blaze = "[Blaze] HP:(65) ATK:(15)"
Helios = "[Helios] HP:(60) ATK:(15)"
Octo = "[Octo] HP:(45} ATK:(12)" """

""" Ray_gun = "[Ray Gun] DMG:(8)"
Fire_sword = "[Fire Sword] DMG:(12)"
Gernade = "[Gernade] DMG:(3)"
The_power_of_the_sun = "[The Power of the Sun] DMG:(10000000000000)" """