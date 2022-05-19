#CIS188_Mike_Lab4.py
'''This Lab is based on the Practice Projects “Fantasy Game Inventory” and "List to Dictionary Function for Fantasy Game Inventory" on page 127 in the textbook.  
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
'''
# I'm using collections to help with the list and get a solid count of items
from collections import Counter

# will display any inventory passed into it
def displayInventory(inventory):
  print("Inventory:")
  count = 0
  for item in inventory:
    print(str(inventory[item]) + " " + str(item) )
    count = count + inventory[item]
  print('Total number of items: ', count)
  # reset counter just because
  count = 0
  

def addToInventory(inventory, addedItems):
    # if passed in two dicts it will put them together
   if(type(addedItems) is  dict):
    for item in addedItems:
      inventory.setdefault(item, 0)
      inventory[item] = inventory[item] + addedItems[item]
      print('Awarded ' + 'item: ' + str(item) + '! New amount: ' + str(addedItems[item]))

    # If passed a list it will read the list, get a count and add them to the inventory
   if(type(addedItems) is  list):
    # Create a temp dict for the recieved items
    tempItems = Counter(addedItems)
    #print(tempItems)
    for item in tempItems:
      inventory.setdefault(item, 0)
      inventory[item] = inventory[item] + tempItems[item]
      print('Awarded ' + 'item: ' + str(item) + '! New amount: ' + str(tempItems[item]))
    


def main(): 

    #Initial inventory
    inventory = {'rope':1,'torch':6,'gold coin':42,'dagger': 1,'arrow':12}
    displayInventory(inventory)

    #Second inventory to test dicts
    #inventory2 = {'rope':1,'torch':6,'gold coin':42,'dagger': 1,'arrow':12, 'sword':1,'tamborine':33}
    #addToInventory(inventory, inventory2)
    #displayInventory(inventory2)
    #displayInventory(inventory)

    #List to be added to inventory
    inventory3 = ['rope', 'sword', 'sword','secretkey','c(o.O)o','Demon soul', '~mace~' ]
    addToInventory(inventory, inventory3)
    print('Congratulations! You\'ve completed the secret quest and you gain a new mystery')
    displayInventory(inventory)
main()