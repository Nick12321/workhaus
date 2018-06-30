import datetime
DATE = datetime.datetime.now()

class Item:

    def __init__(self):
        self.newItem = []

    def addItem(self, newItem):
        Factory.addFactoryItem(self.newItem)


class Factory:

    def __init__(self):
        self.list_of_items = []
        self.items_on_the_list = 0

    def addFactoryItem(self, item_attribute_list):
        self.list_of_items.append(item_attribute_list)
        self.items_on_the_list = self.items_on_the_list + 1

    def printItemList(self):
        itemPrint = 0
        numberOfItems = (self.items_on_the_list - 1)
        while itemPrint < numberOfItems:
            print(self.list_of_items[itemPrint][0] + ", " + self.list_of_items[itemPrint][1] + ", " +self.list_of_items[itemPrint][2])
            itemPrint += 1

item = Item()
newItem = []
newItem = ['iPhone', '', 'X1Y']
item.addItem(newItem)
newItem = ['Samsung s5', '', 'X2A']
item.addItem(newItem)
newItem = ['Orange Juice', '2018, 6, 20', 'X1Y']
item.addItem(newItem)
newItem = ['Veggie Juice', '2019, 6, 20', 'Z3Z']
item.addItem(newItem)
newItem = ['School Bag', '', 'Y2A']
item.addItem(newItem)
item.printItemList()
