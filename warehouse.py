import datetime
DATE = datetime.datetime.now()

class Item:
    def __init__(self, itemName, label, postalCode, area):
        self.itemName = itemName
        self.label = label
        self.postalCode = postalCode
        self.area = area

    def addItem(self, itemName, label, postalCode, area):
        itemList = []
        itemList.append(itemName)
        Item(itemName, label, postalCode, area)

    def listAllItems(self):
        return self.itemName + ', ' + self.label + ', ' + self.postalCode + ', ' + self.area


item1 = Item('iPhone', 'a', 'X1Y', 'A1')
print(item1.listAllItems())
