class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

class linkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
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
body1 = "Four score and twenty years ago"
body2 = "Get busy living or get busy dieing"
body3 = "Life is what happens when you're busy making other plans"
body4 = "Twenty years from now you will be more disappointed by the things you didnt do than the things you did do"
body5 = "Great minds discuss ideas; average minds discuss events; small minds discuss people"
list.insert(body1)
list.insert(body2)
list.insert(body3)
list.insert(body4)
list.insert(body5)
print('here')
