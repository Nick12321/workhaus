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
        print(tempList[0] + ", (" + tempList[1] + "), " + tempList[2])

class Factory:
    def __init__(self):
        self.listOfItems = []
        self.itemsOnTheList = 0

    def addItemToFactoryList (self, itemListToAdd):
        self.listOfItems.append(itemListToAdd)
        self.itemsOnTheList += self.itemsOnTheList
        print("==========")
        print(self.itemsOnTheList)



item = Item()
item1 = item.addItem("iPhone", "", "X1Y")
item2 = item.addItem("Samsung s5", "", "X2A")
item3 = item.addItem("Orange Juice", "2018-06-20", "X1Y")
item4 = item.addItem("Veggie Juice", "2019-06-20", "Z3Z")
item5 = item.addItem("School Bag", "", "Y2A")
