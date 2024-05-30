class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def display_items(self):
        print("Available items in the shop:")
        for idx, item in enumerate(self.items):
            print(f"{idx + 1}. {item.name} - ${item.price}")
    
    def purchase_item(self, item_index, player):
        if item_index < 1 or item_index > len(self.items):
            print("Invalid item selection.")
            return
        
        item = self.items[item_index - 1]
        if player.money >= item.price:
            player.money -= item.price
            player.inventory.append(item)
            print(f"{player.name} purchased {item.name} for ${item.price}. Remaining money: ${player.money}")
        else:
            print("Not enough money to purchase this item.")
    
class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.inventory = []

def main():
    # Create shop and items
    shop = Shop()
    shop.add_item(Item("Sword", 50))
    shop.add_item(Item("Shield", 30))
    shop.add_item(Item("Potion", 10))
    shop.add_item(Item("M16A3", 70))
    shop.add_item(Item("Ray_Gun", 15))
    shop.add_item(Item("Grenade", 5))
    shop.add_item(Item("The Power of the Sun", 1000))
    
    # Create player
    player = Player("Hero", 100)
    
    while True:
        print("\nWelcome to the shop!")
        shop.display_items()
        print(f"\n{player.name}'s money: ${player.money}")
        print("Enter the number of the item you want to buy or '0' to exit:")
        
        try:
            choice = int(input("Your choice: "))
            if choice == 0:
                break
            shop.purchase_item(choice, player)
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\n{player.name}'s inventory:")
    for item in player.inventory:
        print(f"- {item.name}")

if __name__ == "__main__":
    main()