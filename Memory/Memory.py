import random
import time
class Memory:

    def __init__(self):
        self.colNum = 1
        while self.colNum % 2 != 0:
            self.colNum = input("Welcome to Memory!  Please choose the width of your square board (must an even number).")
        self.data = [ [' ']*self.colNum for row in range(self.colNum) ]
        self.numData= []
        self.pairs = []
        #self.answerData
        self.createBoard()

    def __repr__(self):
        H = self.colNum
        W = self.colNum

        s = ""
        colCounter = 1
        for row in range(0,H):
            if self.colNum > 8 and row < 9:
                s += str(colCounter) + '  |'
            else:
                s += str(colCounter) + ' |'
            colCounter += 1
            for col in range(0,W):
                    s += str(self.data[row][col]) + '|'
            s += '\n'

        #s += (2*W+1) * '-'    # bottom of the board
        s += '  '
        x = 1
        if self.colNum < 10:
            s += "  "
        else:
            s += "   "
        s += str(x)
        for i in range(W - 1):
                x += 1
                if self.colNum > 9 and i > 8:
                    s += "  "
                else:
                    s += "   "
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
                    #self.data[row][col] = str(self.numData[i]) + " "
                    self.data[row][col] = " * "
                else:
                    #self.data[row][col] = str(self.numData[i])
                    self.data[row][col] = " * "
                i += 1
        self.hostGame()

    def generateLocation(self):
        location = random.randint(0,self.colNum)
        return location

    def hostGame(self):
        isPlaying = True
        while (isPlaying):
            print self
            user_input = raw_input("Please choose a space to reveal in the format 'row,column'.")
            inputArray = user_input.split(',')
            chosenRow = int(inputArray[0]) - 1
            chosenColumn = int(inputArray[1]) - 1
            numString = str(chosenColumn)
            #self.data[row][col] = str(self.numData[i]) + " "
            H = self.colNum
            W = self.colNum
            i = 0
            for row in range(H):
                for col in range(W):
                    numString = str(self.numData[i])
                    if row == chosenRow and col == chosenColumn:
                        for pair in self.pairs:
                            #print pair
                            dataRow = pair[0]
                            dataCol = pair[1]
                            dataVal = pair[2]
                            if len(str(dataVal)) == 1:
                                self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                            else:
                                self.data[dataRow][dataCol] = " " + str(dataVal)
                        if len(numString) == 1:
                            self.data[row][col] = " " + str(self.numData[i]) + " "
                            #self.data[row][col] = " * "
                        else:
                            self.data[row][col] = str(self.numData[i]) + " "
                            #self.data[row][col] = " * "
                        chosenValue = self.data[row][col]
                        firstChosenNum = chosenValue
                        firstRow = row
                        firstColumn = col
                    i += 1
            print self
            self.printBlankBoard()
            botRow = self.generateLocation()
            botCol = self.generateLocation()
            for botRow in range(H):
                for botCol in range(W):
                    numString = str(self.numData[i])
                    if row == chosenRow and col == chosenColumn:
                        for pair in self.pairs:
                            #print pair
                            dataRow = pair[0]
                            dataCol = pair[1]
                            dataVal = pair[2]
                            if len(str(dataVal)) == 1:
                                self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                            else:
                                self.data[dataRow][dataCol] = " " + str(dataVal)
                        if len(numString) == 1:
                            self.data[row][col] = " " + str(self.numData[i]) + " "
                            #self.data[row][col] = " * "
                        else:
                            self.data[row][col] = str(self.numData[i]) + " "
                            #self.data[row][col] = " * "
                        chosenValue = self.data[row][col]
                        firstChosenNum = chosenValue
                        firstRow = row
                        firstColumn = col
                    i += 1
            print self
            user_input = raw_input("Please choose a second space to reveal in the format 'row,column'.")
            inputArray = user_input.split(',')
            chosenRow = int(inputArray[0]) - 1
            chosenColumn = int(inputArray[1]) - 1
            numString = str(chosenColumn)
            #self.data[row][col] = str(self.numData[i]) + " "
            H = self.colNum
            W = self.colNum
            i = 0
            for row in range(H):
                for col in range(W):
                    numString = str(self.numData[i])
                    if row == chosenRow and col == chosenColumn:
                        if len(numString) == 1:
                            self.data[row][col] = " " + str(self.numData[i]) + " "
                            #self.data[row][col] = " * "
                        else:
                            self.data[row][col] = str(self.numData[i]) + " "
                            #self.data[row][col] = " * "
                        chosenValue = self.data[row][col]
                        secondChosenNum = chosenValue
                        secondRow = row
                        secondColumn = col
                    i += 1
            print self
            if self.checkForPairs(firstChosenNum, secondChosenNum, chosenValue, firstRow, firstColumn, secondRow, secondColumn):
                if self.checkForEnd():
                    print "Congratulations!  You have found all the pairs!"
                    break
                else:
                    print "Congratulations, you found a pair!"
            else:
                print "Sorry, the two values you chose are not a pair."
            #check if all pairs have been found
            time.sleep(2)
            self.printBlankBoard()

    def checkForPairs(self, p1, p2, chosenVal, row1, col1, row2, col2):
        if p1 == p2:
            self.pairs += [[row1, col1, chosenVal]]
            self.pairs += [[row2, col2, chosenVal]]
            #print self.pairs
            return True
        else:
            return False

    def checkForEnd(self):
        H = self.colNum
        W = self.colNum
        i = 0
        for row in range(H):
            for col in range(W):
                if "*" in self.data[row][col]:
                    i += 1
        if i == 0:
            return True
        else:
            return False

    def printBlankBoard(self):
        H = self.colNum
        W = self.colNum
        i = 0
        print self.pairs
        for row in range(H):
            for col in range(W):
                for pair in self.pairs:
                    #print pair
                    dataRow = pair[0]
                    dataCol = pair[1]
                    dataVal = pair[2]
                    if len(str(dataVal)) == 1:
                        self.data[dataRow][dataCol] = str(dataVal) + " "
                    else:
                        self.data[dataRow][dataCol] = str(dataVal)
                numString = str(self.numData[i])
                if len(numString) == 1:
                    #self.data[row][col] = str(self.numData[i]) + " "
                    self.data[row][col] = " * "
                else:
                    #self.data[row][col] = str(self.numData[i])
                    self.data[row][col] = " * "
                i += 1


my = Memory()

#print my