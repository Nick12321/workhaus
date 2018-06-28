import datetime
DATE = datetime.datetime.now()

class Item:

    def __init__(self, itemName, label, postalCode, area):
        self.itemName = itemName
        self.label = label
        self.postalCode = postalCode
        self.area = area
        allItems = []

    def addItem(self, newItem):
        self.allItems.append(newItem)

    def listAllItems(self):
        return self.itemName + ', ' + self.label + ', ' + self.postalCode + ', ' + self.area

#item1 = Item('iPhone', 'a', 'X1Y', 'A1')
newItem = []
newItem = ['iPhone', 'a', 'X1Y', 'A1']
item = Item()
item.addItem(newItem)
print(item1.listAllItems())
