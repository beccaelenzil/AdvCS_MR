class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def parChecker(self, string):
         s = Stack()
         #myList = list(string)
         #parenCounter = 0
         #for i in range(len(myList)):
         #    parenCounter += 1
         #if parenCounter % 2 == 0:
         #    return True
         #else:
         #    return False
         for p in string:
            if p == "(":
                s.push(p)
            elif p == ")":
                if s.isEmpty():
                    return False
                else:
                    s.pop()

         if s.isEmpty():
            return True
         else:
            return False

     def balSymChecker(self, string):
         s = Stack()
         #myList = list(string)
         #parenCounter = 0
         #for i in range(len(myList)):
         #    parenCounter += 1
         #if parenCounter % 2 == 0:
         #    return True
         #else:
         #    return False
         for p in string:
            if p == "([{":
                s.push(p)
            elif p == ")]}":
                if s.isEmpty():
                    return False
                else:
                    s.pop()
         if s.isEmpty():
            return True
         else:
            return False

     def parChecker(self, symbolString):
        s = Stack()
        #instatiate new stack
        balanced = True
        index = 0
        while index < len(symbolString) and balanced:
            symbol = symbolString[index]
            if symbol in "([{":
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    top = s.pop()
                    if not self.matches(top,symbol):
                           balanced = False
            index = index + 1

        if balanced and s.isEmpty():
            return True
        else:
            return False

     def matches(self, open,close):
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

     def divideByTwo(self, number, base):
         s = Stack()
         binaryString = ""
         while number > 0:
             rem = number % base
             number = number // base
             s.push(rem)

         while s.size() > 0:
             binaryString = binaryString + str(s.pop())

         return binaryString




s=Stack()
print s.divideByTwo(26, 2)
#print "parChecker('((()))') == True: ", s.parChecker('((()))')
#print "parChecker('{{([][])}()}') == True: ", s.parChecker('{{([][])}()}')
#print "balSymChecker('{{([][])}()}') == True: ", s.balSymChecker('{{([][])}()}')
#print "balSymChecker('[{()]') == False: ",  s.balSymChecker('[{()]')
# Yes, all of these outcomes are expected