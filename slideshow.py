class Node(object):

    def __init__(self, title, data, counter):
        self.title = None    #For validity check (if this is still None after creating the node, then one of the cases below didn't work out)

        if not isinstance(title, str):          #checks if title is string
            print("This is not a valid Title")
            return

        if not isinstance(data, str):           #checks if body is string
            print("This is not a valid body")
            return

        if not isinstance(counter, int):        #checks if counter is int
            print("This is not a valid ID")
            return

        self.title = title
        self.data = data
        self.id = counter
        self.nextNode = None
        self.previousNode = None
        print("ID: " + str(self.id) + " Title: " + self.title + ", Body: " + self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext): #oldHead is the same as newNext
        self.nextNode = newNext

    def setPrev(self, newPrev):
        self.previousNode = newPrev #newPrev is the same as newHead

    def isValid(self):      #returns a true of false if the node has valid values
        if self.title != None:
            return True
        else:
            return False


class Trash(object):        #implements everything in node, this is for checking the validity of the object we are inserting to the linked list

    def __init__(self, title, data, counter, nextNode=None, previousNode=None):
        self.title = title
        self.data = data
        self.id = counter
        self.nextNode = nextNode
        self.previousNode = previousNode
        print("ID: " + str(self.id) + " Title: " + self.title + ", Body: " + self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext): #oldHead is the same as newNext
        self.nextNode = newNext

    def setPrev(self, newPrev):
        self.previousNode = newPrev #newPrev is the same as newHead

class linkedList(object):
    def __init__(self, head=None, tail=None, current=None):
        self.head = head
        self.tail = tail
        self.current = current

    def insert(self, newNode):
        if not isinstance(newNode, Node):           #Checks if the object we were passed is a Node
            print("This is not a valid Node")
            return

        if not newNode.isValid():                   #Checks if the node has valid values
            print("This is not a valid Node")
            return

        if self.head == None and self.tail == None: #If it is the very first item to be inserted to the list, set current, head, and tail, to the new node
            self.current = newNode
            self.head = newNode
            self.tail = newNode
        else:                                       #If it is not the first item on the list, insert after current
            newNode.setPrev(self.current)
            newNode.setNext(self.current.nextNode)

            if self.current != self.tail:           #Special case! If you are at the tail no need to set the next node to point towards the new node
                self.current.nextNode.setPrev(newNode)

            self.current.setNext(newNode)

            if self.current == self.tail:           #Updating the tail
                self.tail = newNode

    def getCurrentID(self):             #Print current's ID
        if self.current == None:
            print("No items in linked list")
        else:
            print(self.current.id)

    def getCurrentHeadID(self):         #Print Head's ID
        if self.head == None:
            print("No items in linked list")
        else:
            print(self.head.id)

    def getCurrentTailID(self):         #Print Tail's ID
        if self.tail == None:
            print("No items in linked list")
        else:
            print(self.tail.id)

    def goToPrevNode(self):
        if self.current != self.head:
            self.current = self.current.previousNode

    def goToNextNode(self):
        if self.current != self.tail:
            self.current = self.current.nextNode

    def delete(self):               #Delete current node
        if self.head == self.tail:  #If you are the last node, or there no nodes, make current, head, and tail to point to None
            self.head = None
            self.tail = None
            self.current = None
        else:                       #If there are more than 1 nodes
            if self.current == self.tail:           #If current node is the tail, delete current node and set previous node as tail and current, and make its next point to none
                self.current.previousNode.setNext(None)
                self.tail = self.current.previousNode
                self.current = self.tail

            elif self.current == self.head:         #If current node is the head, delete current node and set next node as head and current, and make its previous point to none
                self.current.nextNode.setPrev(None)
                self.head = self.current.nextNode
                self.current = self.head

            else:                                   #If you are on the middle, delete the current node, redirect the previous and next node's next and previous node respectively. Afterwards, set the current to the previous node.
                self.current.previousNode.setNext(self.current.nextNode)
                self.current.nextNode.setPrev(self.current.previousNode)
                self.current = self.current.previousNode



list = linkedList()
counter = 0
title1 = "Abraham Lincoln"
title2 = "Shawshank"
title3 = "John Lennon"
title4 = "Mark Twain"
title5 = "Eleanor Roosevelt"
title6 = 12
title7 = "Eleanor Roosevelt"
title8 = "Eleanor Roosevelt"
body1 = "Four score and twenty years ago"
body2 = "Get busy living or get busy dieing"
body3 = "Life is what happens when you're busy making other plans"
body4 = "you will be more disappointed by what you didnt do than what you did"
body5 = "Great minds discuss ideas; average minds discuss events"
body6 = "Life is what happens when you're busy making other plans"
body7 = 56
body8 = "Life is what happens when you're busy making other plans"
node = Node(title1, body1, counter)
list.insert(node)
counter += 1
node = Node(title2, body2, counter)
list.insert(node)
counter += 1
node = Node(title3, body3, counter)
list.insert(node)
counter += 1
node = Node(title4, body4, counter)
list.insert(node)
counter += 1
node = Node(title5, body5, counter)
list.insert(node)

counter += 1
trash = Trash(title1, body1, counter)
list.insert(trash)

counter += 1
node = Node(title6, body6, counter)
list.insert(node)

counter += 1
node = Node(title7, body7, counter)
list.insert(node)

counter += 1
node = Node(title8, body8, "Hello")
list.insert(node)

list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.delete()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.goToPrevNode()
list.getCurrentID()
list.goToPrevNode()
list.getCurrentID()
list.delete()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.goToPrevNode()
list.getCurrentID()
list.goToPrevNode()
list.getCurrentID()
list.delete()
list.getCurrentID()
list.goToPrevNode()
list.getCurrentID()
list.goToNextNode()
list.getCurrentID()
list.delete()
list.getCurrentID()
list.delete()
list.getCurrentID()
