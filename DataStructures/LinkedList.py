class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, myItem):
        myTempNode = Node(myItem)
        myTempNode.setNext(self.head)
        self.head = myTempNode

    def size(self):
        current = self.head
        count = 0
        while (current != None):
            count += 1;
            current = current.getNext()
        return count

    def search(self, item):
        found = False
        current = self.head
        while (found == False and current.getNext() != None):
            if (current.data == item):
                found = True;
            else:
                current = current.getNext();
        return found

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while (found == False and current.getNext() != None):
            if (current.data == item):
                found = True;
                if (previous != None):
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()

            else:
                previous = current
                current = current.getNext();

#temp = Node(93)
myList = LinkedList()
myList.add(23)
myList.add(56)

myList.remove(56)
print myList.size()