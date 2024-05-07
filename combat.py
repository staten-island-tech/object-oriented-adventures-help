from character import Character

hero = Character(name="Hero", health=100, damage=10)
enemy = Character(name="slime", health=30, damage=3)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health} )