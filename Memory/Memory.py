import random
class Memory:

    def __init__(self):
        self.colNum = input("Welcome to Memory!  Please choose the size of your board.")
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
                    s += self.data[row][col] + '|'
            s += '\n'

        #s += (2*W+1) * '-'    # bottom of the board
        s += '  '
        x = 0
        for i in range(W):
                x += 1
                s += " "
                s += str(x)
           # the string to return
        # and the numbers underneath here

        return s

    def createBoard(self):
        for i in range(0, self.colNum):
            self.numData.append(i)
            self.numData.append(i)
        random.shuffle(self.numData)
        H = self.colNum
        W = self.colNum
        i = 0
        for row in range(0,H-1):
            for col in range(0,W-1):
                self.data[row][col] = self.numData[2*row+col]
                print row,col

        self.hostGame()

    def hostGame(self):
        print self
        user_input = raw_input("Please choose a space to reveal in the format 'row,column'.")
        inputArray = user_input.split(',')
        chosenRow = int(inputArray[0])
        chosenColumn = int(inputArray[1])



my = Memory()

print my