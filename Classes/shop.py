# Define an item class to store item details
class Item:
  def __init__(self, name, price , descripiton):
    self.name = name
    self.price = price
    self.description = descripiton


def currencyfinal()
      currency - item_to_buy.price = currency_final

# Create some sample items
potion = Item("Healing Potion", 30, "❤️🩹" )
sword = Item("Fire Sword" , 100 ,"🔥🔥🔥")
armor = Item("Leather Armor", 80  ,"🛡️")

# Define the shop function
def shop(inventory, currency):
  # Display items and prices
  print("Welcome to the shop!")
  for item in [potion, sword, armor]:
    print(f"{item.name}:,  {item.price} gold" ,item.description )

  # Get user input for purchase
  while True:
    choice = input("What would you like to buy? (or 'b' to leave) ")
    if choice == "b":
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
print("Remaining gold:", )
