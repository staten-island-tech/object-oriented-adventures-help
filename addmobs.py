import json
import os 
class MyClass:
    def __init__(self, mob_name, mob_hp, mob_atk ):
        self.name = mob_name
        self.hp = mob_hp
        self.atk = mob_atk
       

    def to_dict(self):
        return {
            'name': self.name,
            'mob_hp': self.hp,
            'mob_atk': self.atk ,
        }

data = []

# Load existing data if file exists
if os.path.exists('mobs.json'):
    with open('mobs.json', 'r') as file:
        data = json.load(file)

while True:
    name = input("Enter MOB name: ")
    mob_hp = input("Enter Mob HP : ")
    mob_atk = input("Enter Mob attack DMG")
    obj = MyClass(name,mob_hp,mob_atk)
    data.append(obj.to_dict())

    more = input("Do you want to add more? (y/n): ")
    if more.lower() != 'y':
        break

# Write the combined data to the file
with open('mobs.json', 'w') as file:
    json.dump(data, file, indent=4)





