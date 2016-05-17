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
        self.botPairs = []
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
        self.botData = self.numData
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
<<<<<<< Updated upstream
=======
        #Generate random number for bot
>>>>>>> Stashed changes
        location = random.randint(1,self.colNum)
        return location

    def hostGame(self):
        isPlaying = True
        while (isPlaying):
            print self
            #While neither the user nor the bot has won, the hostGame method keeps looping and the human and the bot keep taking turns
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
            print self
            if self.checkForPairs(firstChosenNum, secondChosenNum, firstRow, firstColumn, secondRow, secondColumn):
                if self.checkForEnd():
                    print "Congratulations!  You won!"
                    break
                else:
                    print "Congratulations, you found a pair!"
            else:
                print "Sorry, the two values you chose are not a pair."

            self.printBlankBoard()
            botRow = self.generateLocation()
            botCol = self.generateLocation()
            j = 0
            for bRow in range(self.colNum):
                for bCol in range(self.colNum):
                    if bRow == botRow and bCol == botCol:
                        for pair in self.botPairs:
                            #print pair
                            dataRow = pair[0]
                            dataCol = pair[1]
                            dataVal = pair[2]
                            if len(str(dataVal)) == 1:
                                self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                            else:
                                self.data[dataRow][dataCol] = " " + str(dataVal)
                        if len(numString) == 1:
                            self.data[botRow][botCol] = " " + str(self.numData[j]) + " "
                            #print self.numData[j]
                                #self.data[row][col] = " * "
                        else:
                            self.data[botRow][botCol] = str(self.numData[j]) + ""
                            #print self.numData[j]
                                #self.data[row][col] = " * "
                        print "setting botfirstChosenNum"
                        botChosenValue = self.data[botRow][botCol]
                        botFirstChosenNum = botChosenValue
                        botFirstRow = botRow
                        botFirstColumn = botCol
                    j += 1
            botRow = self.generateLocation()
            botCol = self.generateLocation()
            j = 0
            for bRow in range(self.colNum):
                for bCol in range(self.colNum):
                    if bRow == botRow and bCol == botCol:
                        for pair in self.botPairs:
                            #print pair
                            dataRow = pair[0]
                            dataCol = pair[1]
                            dataVal = pair[2]
                            if len(str(dataVal)) == 1:
                                self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                            else:
                                self.data[dataRow][dataCol] = " " + str(dataVal)
                        if len(numString) == 1:
                            self.data[botRow][botCol] = " " + str(self.numData[j]) + " "
                            #print self.numData[j]
                                #self.data[row][col] = " * "
                        else:
                            self.data[botRow][botCol] = str(self.numData[j])
                            #print self.numData[j]
                                #self.data[row][col] = " * "
                        botChosenValue = self.data[botRow][botCol]
                        botSecondChosenNum = botChosenValue
                        botSecondRow = botRow
                        botSecondColumn = botCol
                    j += 1
            print self
            if self.checkForBotPairs(botFirstChosenNum, botSecondChosenNum, botFirstRow, botFirstColumn, botSecondRow, botSecondColumn):
                if self.checkForBotEnd():
                    print "Sorry!  The bot found all the pairs first!"
                    break
                else:
                    print "Oh no!  The bot found a pair!"
            else:
                print "Yay!  The bot did not find a pair!"
            #check if all pairs have been found
            time.sleep(2)
            self.printBlankBoard()

    def checkForPairs(self, p1, p2, row1, col1, row2, col2):
        if p1 == p2:
            self.pairs += [[row1, col1, p1]]
            self.pairs += [[row2, col2, p2]]
            #print self.pairs
            return True
        else:
            return False

    def checkForBotPairs(self, p1, p2, row1, col1, row2, col2):
        if p1 == p2:
            self.botPairs += [[row1, col1, p1]]
            self.botPairs += [[row2, col2, p2]]
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

    def checkForBotEnd(self):
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
        #print self.pairs
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

        print self#


my = Memory()

#print my