def addToInventory(inventory, addedItems):
    total = 0
    for i in range(len(dragonLoot)): # check dragonLoot to see if there is a match
        for k in inv.keys(): # add 1 to the value if it is found in inv
            if inv.keys() in dragonLoot:
                return (inv.values() + 1)
            else:
                return str(addedItems)
                return(total + 1)

def displayInventory(inventory):
    print('Inventory: ')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v, k))
        itemTotal += str(v)

    print('Total number of items: ' + str(itemTotal))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
