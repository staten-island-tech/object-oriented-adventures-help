# Define an item class to store item details
class Item:
  def __init__(self, name, price , descripiton):
    self.name = name
    self.price = price
    self.description = descripiton


# Create some sample items
potion = Item("Healing Potion", 30, "❤️🩹" )
sword = Item("Fire Sword" , 100 ,"🔥🔥🔥")
armor = Item("Leather Armor", 80  ,"🛡️")


# Initialize player inventory and currency
inventory = []
currency = 100

# Run the shop function
shop(inventory, currency)

# Print remaining inventory and currency
print("Your inventory:", inventory)
print("Remaining gold:", currency )