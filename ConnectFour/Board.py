class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!


    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        x = -1
        for i in range(W):
            if x == 9:
                x = 0
                s += " "
                s += str(x)
            else:
                x += 1
                s += " "
                s += str(x)

        # and the numbers underneath here

        return s
        # the board is complete, return it

    def addMove (self, col, ox):
        counterVar = 0
        for i in range(self.height):
            mySpace = self.data[i][col]
            if mySpace == 'O' or mySpace == 'X':
                counterVar += 1
               # print counterVar
        if counterVar <= self.height:
            self.data[self.height - 1 - counterVar][col] = ox

    def clear (self):
        for i in range (self.width):
            for x in range (self.height):
                self.data[x][i] = ' '

    def setBoard(self, moveString):
        nextCh = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col < self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, c):
        if 0 <= c <= self.width:
            counterVar = 0
            for i in range(self.height):
                mySpace = self.data[i][c]
                if mySpace == 'O' or mySpace == 'X':
                    counterVar += 1
               # print counterVar
            if counterVar <= self.height:
                return True
            else:
                return False
        else:
            return False

    def isFull(self):
        for i in range(self.height):
            for x in range(self.width):
                if self.data[i][x] == ' ':
                    return False
                else:
                    return True

    def delMove(self, c):
        counterVar = 0
        for i in range(self.height):
            mySpace = self.data[i][c]
            if mySpace == 'O' or mySpace == 'X':
                counterVar += 1
               # print counterVar
        if counterVar <= self.height:
            self.data[self.height - counterVar][c] = ' '

    def turn (self):
        user_input = input("What is your guess?")

    def winsFor(self, ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True
                    break
                #else:
                    #return False
        #check for vertical wins
        for row in range(0,H-3):
            for col in range (0,W):
                if D[row][col] == ox and D[row+1][col] == ox and D[row+2][col] == ox and D[row+3][col] == ox:
                    return True
                    break
                #else:
                    #return False
        # check for diagonal wins with a positive slope
        for row in range (0, H-3):
            for col in range (0, W-3):
                if D[row][col] == ox and D[row+1][col+1] == ox and D[row+2][col+2] == ox and D[row+3][col+3] == ox:
                    return True
                    break
                #else:
                    #return False
        for row in range (H-1, 2, -1):
            for col in range (0, W-3):
                if D[row][col] == ox and D[row-1][col+1] == ox and D[row-2][col+2] == ox and D[row-3][col+3] == ox:
                    return True
                    break

    def hostGame(self):
        hasWon = False
        while (hasWon == False):
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("X, choose a column: ")
            self.addMove(users_col, 'X')
            print "X's choice: " + str(users_col)
            print self
            xWins = self.winsFor('X')
            if xWins:
                hasWon == True
                print "X has won!"
                break
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("O, choose a column: ")
            self.addMove(users_col, 'O')
            print "O's choice: " + str(users_col)
            print self
            OWins = self.winsFor('O')
            if OWins:
                hasWon == True
                print "O has won!"
                break


my = Board(7,6)
my.hostGame()
#my.addMove(9, 'O')
#my.addMove(9, 'X')
