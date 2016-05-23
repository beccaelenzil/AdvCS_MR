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
        #generate random numbers to put in the data array, self.numData
        for i in range((self.colNum * self.colNum) / 2):
            self.numData.append(i)
            self.numData.append(i)
        random.shuffle(self.numData)
        self.botData = self.numData
        #populate the display array, self.data, with asterisks
        H = self.colNum
        W = self.colNum
        i = 0
        for row in range(H):
            for col in range(W):
                numString = str(self.numData[i])
                #self.data[row][col] = str(self.numData[i]) + " "
                self.data[row][col] = " * "
                i += 1
        self.hostGame()

    def generateLocation(self):

        #Generate random number for bot
        #THIS METHOD IS OBSOLETE

        location = random.randint(1,self.colNum)
        return location

    def hostGame(self):
        isPlaying = True
        while (isPlaying):

            #human logic
            for pair in self.pairs:
                #print existing pairs
                dataRow = pair[0]
                dataCol = pair[1]
                dataVal = pair[2]
                if len(str(dataVal)) == 1:
                    self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                else:
                    self.data[dataRow][dataCol] = str(dataVal)
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
            #user's first choice is printed.  User is then promted to enter their second choice.
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
            #user's second choice is printed.  The game checks if the user found a pair.
            if self.checkForPairs(firstChosenNum, secondChosenNum, firstRow, firstColumn, secondRow, secondColumn):
                if self.checkForEnd():
                    print "Congratulations!  You won!"
                    break
                else:
                    print "Congratulations, you found a pair!"
            else:
                print "Sorry, the two values you chose are not a pair."
            #check if all pairs have been found
            time.sleep(2)
            self.printBlankBoard()


            #Logic for bot's turn
            for pair in self.pairs:
                #print pair
                dataRow = pair[0]
                dataCol = pair[1]
                dataVal = pair[2]
                if len(str(dataVal)) == 1:
                    self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                else:
                    self.data[dataRow][dataCol] = " " + str(dataVal)


            botRow = random.randint(0,self.colNum-1) #self.generateLocation()
            botCol = random.randint(0,self.colNum-1)
            i = 0
            firstVal = 0
            for row in range(self.colNum):
                for col in range(self.colNum):
                    if row == botRow and col == botCol:
                        firstVal = self.numData[i]
                        break
                    i += 1
            #Bot randomly generates a row and column, and finds the corresponding value out of the one-dimensional data array, self.numData

            #print botRow
            #print botCol
            #print firstVal
            #print " "
            #for z in range(len(self.numData)):
            #    print self.numData[z]
            #break

            botRow2 = random.randint(0,self.colNum-1) #self.generateLocation()
            botCol2 = random.randint(0,self.colNum-1)
            #Bot randomly generates a second row and column and makes sure that it is different from the first one.
            while (botRow2 == botRow and botCol2 == botCol):
                botRow2 = random.randint(0,self.colNum-1) #self.generateLocation()
                botCol2 = random.randint(0,self.colNum-1)
            i = 0
            secondVal = 0
            for row in range(self.colNum):
                for col in range(self.colNum):
                    if row == botRow2 and col == botCol2:
                        secondVal = self.numData[i]
                        break
                    i += 1
            #Bot finds corresponding value for the second row and second column

            if self.checkForPairs(firstVal, secondVal, botRow, botCol, botRow2, botCol2):
                #Since the mechanism that checks for wins uses the display array, self.data, we update that here with the latest pairs.
                for pair in self.pairs:
                    #print pair
                    dataRow = pair[0]
                    dataCol = pair[1]
                    dataVal = pair[2]
                    if len(str(dataVal)) == 1:
                        self.data[dataRow][dataCol] = " " + str(dataVal) + " "
                    else:
                        self.data[dataRow][dataCol] = str(dataVal)
                if self.checkForEnd():
                    print "Oh no!  It looks like the bot won."
                    break
                else:
                    print "Rats!  The bot found a pair!"
                    #print self.pairs
            else:
                print "Yay!  The bot did not find a pair!"

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
        #Method is obsolete - this version only uses checkForPairs
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
        #Method is obsolete - this version only uses checkForEnd
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
        #Resets the display array, self.data
        H = self.colNum
        W = self.colNum
        i = 0
        #print self.pairs
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

my = Memory()

#print my