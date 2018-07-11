class Node(object):

    def __init__(self, title = None, data=None, nextNode=None):
        self.title = title
        self.data = data
        self.nextNode = nextNode
        print(" Title: " + self.title + ", Body: " + self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

class linkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, title, data):
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
title1 = "Abraham Lincoln"
title2 = "Shawshank"
title3 = "John Lennon"
title4 = "Mark Twain"
title5 = "Eleanor Roosevelt"
body1 = "Four score and twenty years ago"
body2 = "Get busy living or get busy dieing"
body3 = "Life is what happens when you're busy making other plans"
body4 = "you will be more disappointed by what you didnt do than what you did"
body5 = "Great minds discuss ideas; average minds discuss events"
list.insert(title1, body1)
list.insert(title2, body2)
list.insert(title3, body3)
list.insert(title4, body4)
list.insert(title5, body5)
print('here')
