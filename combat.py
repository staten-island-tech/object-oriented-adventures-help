from character import Hero, Enemy

hero = Hero(name="hero", health=100)
enemy = Enemy(name="enemy", health=30)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"health of {hero.name}: {hero.health}")
    print(f"health of {enemy.name}: {enemy.health}")

    input()

 