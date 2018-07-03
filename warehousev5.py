import datetime
DATE = datetime.datetime.now()

class Item:
    def __init__(self):
        self.listOfItems = []
        self.itemsOnTheList = 0

    def addItem(self, itemName, itemDate, itemPostalCode):
        self.itemName = itemName
        self.itemDate = itemDate
        self.itemPostalCode = itemPostalCode
        tempList = []
        tempList.append(itemName)
        tempList.append(itemDate)
        tempList.append(itemPostalCode)
        self.listOfItems.append(tempList)
        itemPrint = self.itemsOnTheList
        print(itemPrint)
        print(self.listOfItems[itemPrint][0] + ", (" + self.listOfItems[itemPrint][1] + "), " +self.listOfItems[itemPrint][2])
        print(self.listOfItems[itemPrint][1])
        self.itemsOnTheList += 1
        Item.printItem()

    def printItem():
        print(self.itemsOnTheList)


    # def getArea(self):
        # call to Robot
        #itemName = 'heaven'

# class Robot:

    # def __init__(self, itemName)

item = Item()
item1 = item.addItem("iPhone", "", "X1Y")
item2 = item.addItem("Samsung s5", "", "X2A")
item3 = item.addItem("Orange Juice", "2018-06-20", "X1Y")
item4 = item.addItem("Veggie Juice", "2019-06-20", "Z3Z")
item5 = item.addItem("School Bag", "", "Y2A")
