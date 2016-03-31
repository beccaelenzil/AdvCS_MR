import random
class Memory:

    def __init__(self):
        self.colNum = 1
        while self.colNum % 2 != 0:
            self.colNum = input("Welcome to Memory!  Please choose the width of your square board (must an even number).")
        self.data = [ [' ']*self.colNum for row in range(self.colNum) ]
        self.numData= []
        #self.answerData
        self.createBoard()

    def __repr__(self):
        H = self.colNum
        W = self.colNum

        s = ""
        colCounter = 1
        for row in range(0,H):
            s += str(colCounter) + ' |'
            colCounter += 1
            for col in range(0,W):
                    s += str(self.data[row][col]) + '|'
            s += '\n'

        #s += (2*W+1) * '-'    # bottom of the board
        s += '  '
        x = 0
        for i in range(W):
                x += 1
                s += "  "
                s += str(x)
           # the string to return
        # and the numbers underneath here

        return s

    def createBoard(self):
        for i in range((self.colNum * self.colNum) / 2):
            self.numData.append(i)
            self.numData.append(i)
            random.shuffle(self.numData)
            H = self.colNum
            W = self.colNum
            i = 0
            for row in range(H):
                for col in range(W):
                    numString = str(self.numData[i])
                    if len(numString) == 1:
                        print len(self.data)
                        print i
                        #self.data[row][col] = str(self.numData[i]) + " "
                        self.data[row][col] = "*"
                    else:
                        #self.data[row][col] = str(self.numData[i])
                        self.data[row][col] = "*"
                    i += 1
            self.hostGame()


    def hostGame(self):
        print self
        user_input = raw_input("Please choose a space to reveal in the format 'row,column'.")
        inputArray = user_input.split(',')
        chosenRow = int(inputArray[0])
        chosenColumn = int(inputArray[1])
        self.data[chosenRow][chosenColumn] = self.numData[chosenRow][chosenColumn]
        print self




my = Memory()

print my