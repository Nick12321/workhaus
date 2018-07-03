import datetime
DATE = datetime.datetime.now()

class Item:

    def createItem(self, itemName, itemDate, itemPostalCode):
        self.itemName = itemName
        self.itemDate = itemDate
        self.itemPostalCode = itemPostalCode
        tempList = []
        tempList.append(itemName)
        tempList.append(itemDate)
        tempList.append(itemPostalCode)
        return(tempList)

class Factory:
    def __init__(self):
        self.listOfItems = []
        self.itemsOnTheList = 0

    def addItemToFactoryList(self, itemListToAdd):
        self.listOfItems.append(itemListToAdd)
        self.itemsOnTheList += 1

    def getListOfItems(self):
        return(self.listOfItems)

    def printFactoryList(self):
        print(self.listOfItems)


class Robot:
    def __init__(self, ID):
        self.id = ID

class Inspecting(Robot):
    def __init__(self, ID):
        super().__init__(ID)

    def verifyExpiry(self, listOfItems):
        year = DATE.strftime("%Y")
        month = DATE.strftime("%m")
        day = DATE.strftime("%d")
        currentDate = year + "-" + month + "-" + day

        indicesToDelete = []
        deleted = 0
        currentIndex = 0

        for item in listOfItems:
            if (len(item[1]) != 0) and (currentDate > item[1]):
                    indicesToDelete.append(currentIndex)

            currentIndex += 1

        for index in indicesToDelete:
            listOfItems.pop(index - deleted)
            deleted += 1


class Decision(Robot):
    def __init__(self, ID):
        super().__init__(ID)

    def chooseLabelRobot(self, listOfItems):
        toLabelRobot1 = []
        toLabelRobot2 = []
        toLabelRobot3 = []
        toLabelRobot4 = []

        for item in listOfItems:

            if(item[2] == "X1Y" or item[2] == "Y1Y"):
                toLabelRobot1.append(item)
            elif (item[2] == "Y1X" or item[2] == "X2A"):
                toLabelRobot2.append(item)
            elif (item[2] == "Y2A" or item[2] == "Z3Z"):
                toLabelRobot3.append(item)
            else:
                toLabelRobot4.append(item)

        return (toLabelRobot1, toLabelRobot2, toLabelRobot3, toLabelRobot4)



class Labeling(Robot):
    def __init__(self, ID, label):
        super().__init__(ID)
        self.label = label

    def putLabel(self, listOfItems):
        for item in listOfItems:
            item.append(self.label)


item = Item()
factory = Factory()
inspecting = Inspecting("RI-01")
decision = Decision("RD-01")
labeling1 = Labeling("RL-01", "A1")
labeling2 = Labeling("RL-02", "A2")
labeling3 = Labeling("RL-03", "A3")
labeling4 = Labeling("RL-04", "A4")
item1 = item.createItem("iPhone", "", "X1Y")
item2 = item.createItem("Samsung s5", "", "X2A")
item3 = item.createItem("Orange Juice", "2018-06-20", "X1Y")
item4 = item.createItem("Veggie Juice", "2019-06-20", "Z3Z")
item5 = item.createItem("School Bag", "", "Y2A")
factory.addItemToFactoryList(item1)
factory.addItemToFactoryList(item2)
factory.addItemToFactoryList(item3)
factory.addItemToFactoryList(item4)
factory.addItemToFactoryList(item5)
itemList = factory.getListOfItems()
inspecting.verifyExpiry(itemList)
(l1, l2, l3, l4) = decision.chooseLabelRobot(itemList)
labeling1.putLabel(l1)
labeling2.putLabel(l2)
labeling3.putLabel(l3)
labeling4.putLabel(l4)
factory.printFactoryList()
