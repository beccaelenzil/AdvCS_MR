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
        location = random.randint(0,self.colNum)
        return location

    def hostGame(self):

        while True:

            playersTurn = True
            computersTurn = False

            while playersTurn:

                ChosenNum = []
                Row = []
                Col = []

                #3rd tab in, player should choose 2 positions
                print self
                for k in range(2):
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
                                ChosenNum.append(chosenValue)
                                Row.append(row)
                                Col.append(col)
                            i += 1
                    print self

                print Row
                print Col
                print ChosenNum

                #3rd tab in, check for player pairs
                if self.checkForPairs(ChosenNum[0], ChosenNum[1], chosenValue, Row[0], Col[0], Row[1], Col[1]):
                    if self.checkForEnd():
                        print "Congratulations!  You won!"
                        break
                    else:
                        print "Congratulations, you found a pair!\n"
                else:
                    print "Sorry, the two values you chose are not a pair.\n"
                    playersTurn = False
                    computersTurn = True


                print "Now it's the computer turn"
                time.sleep(2)
                self.printBlankBoard()


            while computersTurn:

                botChosenNum = []
                botRowList = []
                botColList = []

                #3rd tab in, bot should get two positions
                for n in range(2):
                    botRow = self.generateLocation()
                    botCol = self.generateLocation()

                    j = 0

                    for bRow in range(H): #this was self.colNum
                        for bCol in range(W): #this was self.rowNum
                            if bRow == botRow and bCol == botCol:
                                #printing existing pairs
                                for pair in self.botPairs:
                                    #print pair
                                    dataRow = pair[0]
                                    dataCol = pair[1]
                                    dataVal = pair[2]
                                    if len(str(dataVal)) == 1:
                                        self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                                    else:
                                        self.data[dataRow][dataCol] = " " + str(dataVal)
                                #printing the newly-chosen pair
                                if len(numString) == 1:
                                    self.data[botRow][botCol] = " " + str(self.numData[j]) + " "
                                    #print self.numData[j]
                                        #self.data[row][col] = " * "
                                else:
                                    self.data[botRow][botCol] = str(self.numData[j]) + ""
                                    #print self.numData[j]
                                        #self.data[row][col] = " * "

                                botChosenValue = self.data[botRow][botCol]
                                botChosenNum.append(botChosenValue)
                                botRowList.append(botRow)
                                botColList.append(botCol)

                            j += 1
                    print self

                print botRowList
                print botColList
                print botChosenNum

                if self.checkForBotPairs(botChosenNum[0], botChosenNum[1], botRowList[0], botColList[1], botRowList[1], botRowList[1]):
                    if self.checkForBotEnd():
                        print "Sorry!  The bot found all the pairs first!\n"
                        break
                    else:
                        print "Oh no!  The bot found a pair!\n"
                else:
                    print "Yay!  The bot did not find a pair!\n"
                    print "Now it's your turn again"
                    computersTurn = False
                    playersTurn = True


                time.sleep(2)

    def checkForPairs(self, p1, p2, chosenVal, row1, col1, row2, col2):
        if p1 == p2:
            self.pairs += [[row1, col1, chosenVal]]
            self.pairs += [[row2, col2, chosenVal]]
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

        print self#


my = Memory()


