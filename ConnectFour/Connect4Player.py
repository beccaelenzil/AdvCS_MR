import random
import sys
from Board import MyBoard

class basicPlayer():
    """a basic player class that selects the next move"""
    def __init__(self, ox):
        """the constructor"""
        self.ox = ox

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Basic player for " + self.ox + "\n"
        return s

    def nextMove(self,b):
        """selects an allowable next move at random"""
        col = -1
        while b.allowsMove(col) == False:
            col = random.randrange(b.width)
        return col

class smartPlayer(basicPlayer):
    """ an AI player for Connect Four """
    def __init__(self, ox):
        """ the constructor inherits from from the basicPlayer class"""
        basicPlayer.__init__(self, ox)

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Smart player for " + self.ox + "\n"
        return s
    def oppCh(self):
        if self.ox == 'O':
            return 'X'
        elif self.ox == 'X':
            return 'O'

    def scoresFor(self, b):
        scores = [50] * b.width
        for col in range(b.width):
            if not b.allowsMove(col):
                scores[col] = -1
            else:
                b.addMove(col, self.ox)
                if b.winsFor(self.ox):
                    scores[col] = 100
                else:
                    for colOpp in range(b.width):
                        if b.allowsMove(colOpp):
                            b.addMove(colOpp, self.oppCh())
                            if b.winsFor(self.oppCh()):
                                scores[col] = 0
                            b.delMove(colOpp)
                b.delMove(col)
        return scores

    def nextMove(self, b):
        scores = self.scoresFor(b)
        maxIndex = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                maxIndex.append(i)
        col = random.choice(maxIndex)
        return col

def playGame(playerX, playerO):

    """
    playerX should be 'basic', 'smart' or 'human'
    playerO should be 'basic', 'smart' or 'human'
    """
    if playerX == 'smart':
        pX = smartPlayer('X')
    elif playerX == 'basic':
        pX = basicPlayer('X')
    elif playerX != 'human':
        print "Player X should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()

    if playerO == 'smart':
        pO = smartPlayer('O')
    elif playerO == 'basic':
        pO = basicPlayer('O')
    elif playerO != 'human':
        print "Player O should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()

    b = MyBoard(7,6)
    #print b

    hasWon = False
    while (hasWon == False):
        users_col = -1
        while b.allowsMove( users_col ) == False:
            if pX == 'human':
                users_col = input("X, choose a column: ")
            else:
                users_col = pX.nextMove(b)

        b.addMove(users_col, 'X')

        #print "X's choice: " + str(users_col)
        #print b

        xWins = b.winsFor('X')
        if xWins:
            hasWon == True
            #print "X has won!"
            return 0
        elif b.isFull():
            hasWon == True
            #print "Tie!"
            return 2
        users_col = -1
        while b.allowsMove( users_col ) == False:
            if pO == 'human':
                users_col = input("O, choose a column: ")
            else:
                users_col = pO.nextMove(b)
        b.addMove(users_col, 'O')
        #print "O's choice: " + str(users_col)
        #print b
        OWins = b.winsFor('O')
        if OWins:
            hasWon == True
            #print "O has won!"
            return 1
        elif b.isFull():
            hasWon == True
            #print "Tie!"
            return 2

print "hi"

#p = playGame('smart', 'smart')
o_x_truce = [0,0,0]
for i in range (100):
    winner = playGame('smart', 'smart')
    o_x_truce[winner] += 1
    print i
print o_x_truce
#print p
#Smart Player for X
