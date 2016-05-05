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
                    if s.pop() ==
                    s.pop()


         if s.isEmpty():
            return True
         else:
            return False




s=Stack()

print "parChecker('((()))') == True: ", s.parChecker('((()))')
print "balSymChecker('{{([][])}()}') == True: ", s.balSymChecker('{{([][])}()}')
print "balSymChecker('[{()]') == False: ",  s.balSymChecker('[{()]')
# Yes, all of these outcomes are expected