import json
import os 
class MyClass:
    def __init__(self, characters_name, characters_hp, characters_atk ):
        self.name = characters_name
        self.hp = characters_hp
        self.atk = characters_atk
       

    def to_dict(self):
        return {
            'name': self.name,
            'characters_hp': self.hp,
            'characters_atk': self.atk ,
        }

data = []

# Load existing data if file exists
if os.path.exists('characters.json'):
    with open('characters.json', 'r') as file:
        data = json.load(file)

while True:
    name = input("Enter characters name: ")
    characters_hp = input("Enter characters HP : ")
    characters_atk = input("Enter characters attack DMG")
    obj = MyClass(name,characters_hp,characters_atk)
    data.append(obj.to_dict())

    more = input("Do you want to add more? (y/n): ")
    if more.lower() != 'y':
        break

# Write the combined data to the file
with open('characters.json', 'w') as file:
    json.dump(data, file, indent=4)





