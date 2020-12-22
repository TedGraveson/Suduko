#Takes 9 * 9 2-D array and creates Suduko game
class Suduko():
    def __init__(self, board):
        self.board = []
        self.selected = (0,0)
        for row in range(len(board)):
            rowToAdd = []
            for col in range(len(board[0])):
                rowToAdd.append(board[row][col])
            self.board.append(rowToAdd)


    def printBoard(self):
        for row in self.board:
            for pos in row:
                print(pos, end=' ') 
            print()
        print()

    def setSquare(self, pos, num) :
        self.board[pos[0]][pos[1]] = num

    def getSquare(self, pos):
        return self.board[pos[0]][pos[1]]

    def selectSquare(self, pos):
        self.selected = pos

    #Finds next empty spot in board
    def nextEmptySpace(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col].getNum() == 0:
                    return self.board[row][col].getSquare().getPos()
        return None

    def checkMove(self, pos, num):
        moveRow = pos[0]
        moveCol = pos[1]
        #Check row
        for checkCol in range(len(self.board[moveRow])):
            print(self.board[moveRow][checkCol])
            if(self.board[moveRow][checkCol] == num):
                print("Row " + str(moveRow) + ", " + str(moveCol))
                return False

        print()
        #Check col
        for checkRow in range(len(self.board[moveCol])):
            print(str(self.board[checkRow][moveCol]))
            if(self.board[checkRow][moveCol] == num):
                print("Col")
                return False

        #Check box
        boxRow = (moveRow // 3) * 3
        boxCol = (moveCol// 3) * 3

        for checkRow in range(boxRow, boxRow+3):
            for checkCol in range(boxCol, boxCol+3):
                if (self.board[checkRow][checkCol] == num):
                    print("box")
                    return False

        return True


arr = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

test = Suduko(arr)
test.printBoard()
print(str(test.checkMove((2,0), 2)))