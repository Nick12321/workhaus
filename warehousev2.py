import datetime
DATE = datetime.datetime.now()

class Item:

    # def __init__(self, itemName, label, postalCode, area):
    #     self.itemName = itemName
    #     self.label = label
    #     self.postalCode = postalCode
    #     self.area = area
    #     self.allItems = []

    def __init__(self):
        self.list_of_items = []
        self.items_on_the_list = 0


    def addItem(self, item_attribute_list):
        self.list_of_items.append(item_attribute_list)
        self.items_on_the_list = self.items_on_the_list + 1
        #self.itemName = item_attribute_list[0]
        #self.label = item_attribute_list[1]
        #self.postalCode = item_attribute_list[2]
        #self.area = item_attribute_list[3]

    def getNumberOfItems(self):
        return (self.items_on_the_list)

    def printItemList(self):
        print(self.list_of_items)


class Factory:

    #def __init__(self):

    def listAllItems(self):
        return self.itemName + ', ' + self.label + ', ' + self.postalCode + ', ' + self.area



#item1 = Item('iPhone', 'a', 'X1Y', 'A1')
newItem = []
newItem = ['iPhone', 'a', 'X1Y', 'A1']
item = Item()
item.addItem(newItem)
newItem = ['iPhoneX', 'a', 'X1Y', 'A1']
item.addItem(newItem)
item.printItemList()

#print(item1.listAllItems())
