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

    def append(self, myItem):
        current = self.head
        while (current.getNext() != None):
                current = current.getNext();
        myTempNode = Node(myItem)
        myTempNode.setNext(None)

    def insert(self, myItem, myIndex):
        found = False
        current = self.head
        counter = 0;
        while (found == False and current.getNext() != None):
            if (counter == myIndex):
                found = True;
                break;
            else:
                current = current.getNext();
                counter += 1
        myTempNode = Node(myItem)
        myTempNode.setNext(current)

    def pop(self):
        found = False
        current = self.head
        previous = None
        while (current.getNext() != None):
            previous = current
            current = current.getNext();
        if (previous != None):
            previous.setNext(None)
        else:
            self.head = None

    def Display(self):
        current = self.head
        myList = [current.data];
        while (current.getNext() != None):
            current = current.getNext();
            myList.append(current.data)
        print myList

    def getAtIndex(self, myIndex):
        found = False
        current = self.head
        counter = 0;
        while (found == False and current.getNext() != None):
            if (counter == myIndex):
                found = True;
                break;
            else:
                current = current.getNext();
                counter += 1
        print current.data

    def

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

#myList.remove(56)
#print myList.size()
myList.Display()