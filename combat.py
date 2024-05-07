from character import Character

hero = Character(name="hero", health=100, damage=10)
enemy = Character(name="enemy", health=30, damage=3)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")

    input()