import datetime
DATE = datetime.datetime.now()

#class Item:

class Factory:
    def __init__(self):
        self.listOfItems = []
        self.itemsOnTheList = 0

    def addItem(self, itemAttributeList):
        self.listOfItems.append(itemAttributeList)
        self.itemsOnTheList = self.itemsOnTheList + 1
        Robot.checkDate()

    def getItemNumber(self):
        print("getItemNumber - itemsOnTheList")
        print(self.itemsOnTheList)
        # why is self.itemsOnTheList 0, when printItemList has the correct #?
        externalItemNum = self.itemsOnTheList
        print(externalItemNum)
        return(externalItemNum)

    def getNumberOfItems(self):
        return (self.itemsOnTheList)

    def printItemList(self):
        itemPrint = 0
        numberOfItems = (self.itemsOnTheList)
        while itemPrint < numberOfItems:
            print('numberOfItems')
            print(numberOfItems)
            print('itemPrint')
            print(itemPrint)
            print(self.listOfItems[itemPrint][0] + ", (" + self.listOfItems[itemPrint][1] + "), " +self.listOfItems[itemPrint][2])
            itemPrint += 1

class Robot:
    def __init__(self):
        self.year = year
        self.month = month
        self.day = day

    def checkDate():
        year = DATE.strftime("%Y")
        month = DATE.strftime("%m")
        day = DATE.strftime("%d")
        print(year + "-" + month + "-" + day)
        factory = Factory()
        robotItemNum = factory.getItemNumber()
        # print(robotItemNum) - why is this 0?


# item = Item()
item = Factory()
newItem = []
newItem = ['iPhone', '', 'X1Y']
item.addItem(newItem)
newItem = ['Samsung s5', '', 'X2A']
item.addItem(newItem)
newItem = ['Orange Juice', '2018-06-20', 'X1Y']
item.addItem(newItem)
newItem = ['Veggie Juice', '2019-06-20', 'Z3Z']
item.addItem(newItem)
newItem = ['School Bag', '', 'Y2A']
item.addItem(newItem)
item.printItemList()
item.getItemNumber()
