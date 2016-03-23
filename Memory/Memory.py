class Memory:

    def __init__(self):
        self.colNum = input("Welcome to Memory!  Please choose the size of your board.")
        self.data = [ [' ']*self.colNum for row in range(self.colNum) ]
        self.hostGame()

    def __repr__(self):
        H = self.colNum
        W = self.colNum

        s = ""
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '* |'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        x = -1
           # the string to return
        # and the numbers underneath here

        return s

    def hostGame(self):
        print self
        user_input = raw_input("Please choose a space to reveal in the format 'row, column'.")
        print type(user_input)
        inputArray = user_input.split(',')
        for myString in inputArray:
            print myString



my = Memory()

print my