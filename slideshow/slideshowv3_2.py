
class Node:
    def __init__(self):
        self.nodeAnchor = nodeAnchor

    def createNode(self, nodeList):
        self.title = nodeList[0]
        self.body = nodeList[1]
        self.next = None
        self.prev = None
        self.id = None
        nodeAnchor = self
        print(" Title: " + self.title + ", Body: " + self.body)

    def nextNode(self, newNode):
        self.id = linkedList().self.itemsOnTheList
        self.next = nodeAnchor


    def printNode(self):
        print("ID = " + str(self.id) + " Title: " + self.title + ", Body: " + self.body)

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.itemsOnTheList = 0

    def addToList(self, newNode):
        if self.itemsOnTheList == 0:
            self.head = newNode
            self.tail = newNode

        else:
            self.itemsOnTheList += 1
            Node().nextNode(newNode)
            self.head = newNode





node1 = ["Abraham Lincoln", "Four score and seven years ago"]
Node().createNode(node1)
node2 = ["Shawshank", "Get busy living or get busy dieing"]
Node().createNode(node2)
node3 = ["John Lennon", "Life is what happens when you're busy making other plans"]
Node().createNode(node3)
node4 = ["Mark Twain", "Twenty years from now you will be more disappointed by the things you didnt do than the things you did do"]
Node().createNode(node4)
node5 = ["Eleanor Roosevelt", "Great minds discuss ideas; average minds discuss events; small minds discuss people"]
Node().createNode(node5)
