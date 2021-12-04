
def readfile(filename):
    with open("input.txt") as file:
        return [line.rstrip() for line in file.readlines()]

# Find's 1st Winner's Score
def bingo1(filename):
    # Read Input
    lines = readfile(filename)

    # Builds Boards
    boards = Boards(list(map(int,lines[0].split(","))))
    i = 2
    while i < len(lines):
        boards.addBoard(lines[i:i+5])
        i += 6

    # Find First Winner's Score
    for i in range(len(lines[0].split(","))):
        boards.removeNumber()
        found, score = boards.checkWinner()
        if found:
            return score

    return -1

# Find's last Winner's Score
def bingo2(filename):
    # Read Input
    lines = readfile(filename)

    # Builds Boards
    boards = Boards(list(map(int,lines[0].split(","))))
    numBoards, i = 0, 2
    while i < len(lines):
        boards.addBoard(lines[i:i+5])
        numBoards += 1
        i += 6

    # Find Last Winner's Score
    lastScore = -1
    for i in range(len(lines[0].split(","))):
        boards.removeNumber()
        found, score = boards.checkWinner()
        if found:
            lastScore = score

    return lastScore

class Board:

    def __repr__(self):
        board = ""
        for row in self.board:
            for digit in row:
                if digit < 10:
                    board += " "
                board += str(digit)+" "
            board += "\n"
        return board

    def __init__(self,board):
        self.board = board
        self.originalBoard = board
        self.isActive = True

    def removeNumber(self,number):
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                if num == number:
                    self.board[i][j] = -1

    def checkWinner(self):
        for row in self.board:
            if sum(row) == -5:
                self.isActive = False
                return True
        for row in [*zip(*self.board)]:
            if sum(row) == -5:
                self.isActive = False
                return True
        return False

    def findScore(self,number):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == -1:
                    continue
                score += self.originalBoard[i][j]
        return score*number

class Boards:

    def __init__(self,numbers):
        self.boards = []
        self.winningBoard = None
        self.numbersIdx = 0
        self.numbers = numbers

    def addBoard(self,board):
        intBoard = []
        for row in board:
            intBoard.append(list(map(int,row.split())))
        self.boards.append(Board(intBoard))

    def printBoards(self):
        for board in self.boards:
            print(board)

    def removeNumber(self):
        for board in self.boards:
            board.removeNumber(self.numbers[self.numbersIdx])
        self.numbersIdx += 1
        
    def checkWinner(self):
        foundWinner = True
        result = (False,0)
        for board in self.boards:
            if not board.isActive: continue
            isWinner = board.checkWinner()
            if foundWinner and isWinner:
                founderWinner = False
                result = (True,board.findScore(self.numbers[self.numbersIdx-1]))
        return result
    
print(bingo1("input.txt"))
print(bingo2("input.txt"))

