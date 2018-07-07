class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addItemToLinkedList(self, value):
        newNode = Node(value)
        print('in addItemToLinkedList')
        if self.tail == None:
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        print(newNode)

    def printLinkedList(self):
        print('in printLinkedList')
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value)
            currentNode = currentNode.next



list = linkedList()
body1 = "Four score and twenty years ago"
body2 = "Get busy living or get busy dieing"
body3 = "Life is what happens when you're busy making other plans"
body4 = "Twenty years from now you will be more disappointed by the things you didnt do than the things you did do"
body5 = "Great minds discuss ideas; average minds discuss events; small minds discuss people"
list.addItemToLinkedList(body1)
list.addItemToLinkedList(body2)
list.addItemToLinkedList(body3)
list.addItemToLinkedList(body4)
list.addItemToLinkedList(body5)
print('here')
list.printLinkedList()
