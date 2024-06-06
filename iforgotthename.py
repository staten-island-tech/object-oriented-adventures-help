from player import Character 
hero = Character(name="hero", health=100) 
enemy = Character(name="enemy", health=30) 
while True: 
    hero.attack(enemy) 
    print(f"health of {hero.name}: {hero.health}") 
    enemy.attack(hero)
    print(f"health of {hero.name}: {hero.health}") 
