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
    shop.add_item(Item("M16A3", 70 ))
    shop.add_item(Item("Ray_Gun", 15))
    shop.add_item(Item("Grenade", 5))
    shop.add_item(Item("The Power of the Sun" , 1000))
    
# Define the shop function
def shop(inventory, currency):
  # Display items and prices
  print("Welcome to the shop!")
  for item in [potion, sword, armor]:
    print(f"{item.name}:,  {item.price} gold" ,item.description )

  # Get user input for purchase
  while True:
    choice = input("Enter the name of the item you want to buy or '0' to exit:")
    if choice == 0: 
      break
    
    # Check for valid item choice
    if choice.lower() in [item.name.lower() for item in [potion, sword, armor]]:
      item_to_buy = next(item for item in [potion, sword, armor] if item.name.lower() == choice.lower())
      # Check if player has enough money
      if currency >= item_to_buy.price:
        inventory.append(item_to_buy.name)  # Add item to inventory
        currency -= item_to_buy.price   # Deduct price from currency
        print(f"You bought {item_to_buy.name}!")
      else:
        print("Insufficient funds!")
    else:
      print("Invalid item choice.")

# Initialize player inventory and currency
inventory = []
currency = 100

# Run the shop function
shop(inventory, currency)

# Print remaining inventory and currency
print("Your inventory:", inventory)
print("Remaining gold:", currency )
