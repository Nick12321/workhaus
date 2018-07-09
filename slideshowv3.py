noOfNodes = 0

class Node:

    def createNode(self, nodeList):
        self.title = nodeList[0]
        self.body = nodeList[1]
        self.head = None
        self.id = noOfNodes
        noOfNodes =+ 1
        print("ID = " + str(self.id) + " Title: " + self.title + ", Body: " + self.body)

    def printNode(self):
        print("Title: " + self.title + ", Body: " + self.body)

# class linkedList:
#     self.head = head
#     self.next = nextNode
#     self.previous = previousNode
#     nodesInList = 0
#
#     def addToList(self, newNode):
#         if nodesInList == 0:
#             print('q')


node1 = ["Abraham Lincoln", "Four score and seven years ago"]
# Node.createNode(["Abraham Lincoln", "Four score and seven years ago"]) - why doesnt this work?
Node().createNode(node1) #works
# Node().createNode("Abraham Lincoln", "Four score and seven years ago")
node2 = ["Shawshank", "Get busy living or get busy dieing"]
Node().createNode(node2)
node3 = ["John Lennon", "Life is what happens when you're busy making other plans"]
Node().createNode(node3)
node4 = ["Mark Twain", "Twenty years from now you will be more disappointed by the things you didnt do than the things you did do"]
Node().createNode(node4)
node5 = ["Eleanor Roosevelt", "Great minds discuss ideas; average minds discuss events; small minds discuss people"]
Node().createNode(node5)
