class Node:
    def __init__(self):
        self.noOfNodes = 0

    def createNode(self, title, body):
        self.title = title
        self.body = body
        self.nextNode = nextNode

    # def __init__(self, data=None, nextNode=None):
    #     self.data = data
    #     self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

class linkedList:
    def __init__(self, title, data):
        self.title = title
        self.data = data
        self.head = head

    def insert(self):
        newNode = Node(title, data)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        current = self.head
        counter = 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
            if current is None:
                raise ValueError("Data not in list")
            return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
            if current is None:
                raise ValueError("Data not in list")
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())


list = linkedList()
node1 = list.insert("Abraham Lincoln", "Four score and seven years ago")
node2 = list.insert("Shawshank", "Get busy living or get busy dieing")
node3 = list.insert("John Lennon", "Life is what happens when you're busy making other plans")
node4 = list.insert("Mark Twain", "Twenty years from now you will be more disappointed by the things you didnt do than the things you did do")
node5 = list.insert("Eleanor Roosevelt", "Great minds discuss ideas; average minds discuss events; small minds discuss people")
print('here')
