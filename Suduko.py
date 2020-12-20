import pygame
from pygame.constants import RESIZABLE


boardImg = pygame.image.load("SudokuBoard900.jpg")
boardImg = pygame.transform.scale(boardImg, (600, 600))
class GridSquare():
    def __init__(self, pos, num):
        self.pos = pos
        self.num = num
        self.selected = False

    def getPos(self):
        return self.pos

    def getNum(self):
        return self.num

    def setNum(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

class Board():
    def __init__(self, board):
        self.boardState = []
        for row in range(len(board)):
            rowToAdd = []
            for col in range(len(board[0])):
                rowToAdd.append(GridSquare((col, row),board[row][col]))
            self.boardState.append(rowToAdd)


    def printBoard(self):
        for row in self.boardState:
            for pos in row:
                print(pos, end=' ') 
            print()
        print()

    #Addressed from left right 
    def setSquare(self, pos, num) :
        self.boardState[pos[0]][pos[1]].setNum(num)

    def getSquare(self, pos):
        return self.boardState[pos[0]][pos[1]]



class SudukoGUI():
    def __init__(self, board):
        pygame.init()
        self.running = True
        self.board = board
        self.windowSize = (900, 600)
        self.boardWidth = 600
        self.boardHeight = 600
        self.screen = pygame.display.set_mode(self.windowSize)
        self.screen.blit(boardImg, (0,0))
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        pygame.display.update()
        self.startGame()

    
    def drawBoard(self):
        for col in range(9):
            for row in range(9):
                self.drawSquare(self.board.getSquare((row, col)))
        pygame.display.update()

    def drawSquare(self, gridSquare):
        #Number to be drawn
        square = self.font.render(str(gridSquare.getNum()), False, (0,0,0))
        print(gridSquare.getPos()[0])
        print(gridSquare.getPos()[1])
        print(self.windowSize[0]/3)
        boardWidth = self.windowSize[0]-(self.windowSize[0]/3)
        boardHeight = self.windowSize[1]
        xPos = boardWidth/9 * gridSquare.getPos()[1]
        yPos = boardHeight/9 * gridSquare.getPos()[0]
        self.screen.blit(square, (xPos, yPos))
        
        

    def startGame(self):
        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.drawBoard()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    row = -1
                    col = -1
                    if pos[0] < self.boardWidth/9:
                        col = 0
                    elif pos[0] >= self.boardWidth/9 * 1 and pos[0]  < self.boardWidth/9 *2:
                        col = 1
                    elif pos[0] >= self.boardWidth/9 * 2 and pos[0]  < self.boardWidth/9 *3:
                        col = 2
                    elif pos[0] >= self.boardWidth/9 * 3 and pos[0]  < self.boardWidth/9 *4:
                        col = 3
                    elif pos[0] >= self.boardWidth/9 * 4 and pos[0]  < self.boardWidth/9 *5:
                        col = 4
                    elif pos[0] >=self.boardWidth/9 * 5 and pos[0]  < self.boardWidth/9 *6:
                        col = 5
                    elif pos[0] >= self.boardWidth/9 * 1 and pos[0]  < self.boardWidth/9 *7:
                        col = 6
                    elif pos[0] >= self.boardWidth/9 * 7 and pos[0]  < self.boardWidth/9 *8:
                        col = 7
                    elif pos[0] >= self.boardWidth/9 * 8 and pos[0]  <= self.boardWidth/9 *9:
                        col = 8
                    print(col)
                    if pos[1] < self.boardHeight/9:
                        row = 0
                    elif pos[1] >= self.boardHeight/9 * 1 and pos[1]  < self.boardHeight/9 *2:
                        row = 1
                    elif pos[1] >= self.boardHeight/9 * 2 and pos[1]  < self.boardHeight/9 *3:
                        row = 2
                    elif pos[1] >= self.boardHeight/9 * 3 and pos[1]  < self.boardHeight/9 *4:
                        row = 3
                    elif pos[1] >= self.boardHeight/9 * 4 and pos[1]  < self.boardHeight/9 *5:
                        row = 4
                    elif pos[1] >= self.boardHeight/9 * 5 and pos[1]  < self.boardHeight/9 *6:
                        row = 5
                    elif pos[1] >= self.boardHeight/9 * 1 and pos[1]  < self.boardHeight/9 *7:
                        row = 6
                    elif pos[1] >= self.boardHeight/9 * 7 and pos[1]  < self.boardHeight/9 *8:
                        row = 7
                    elif pos[1] >= self.boardHeight/9 * 8 and pos[1]  <= self.boardHeight/9 *9:
                        row = 8
                    print(row)
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((self.screen.get_width(),self.screen.get_height()), pygame.RESIZABLE)
                    self.screen.blit(boardImg, (0,0))
                    pygame.display.update()


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
    
# class Suduko():
#     def __init__(self, board):
#         self.board = []
#         for row in range(9):
#             rowToAdd = []
#             for col in range(9):
#                 rowToAdd.append(board[row][col])
#             self.board.append(rowToAdd)

    



test = Board(arr)
suduko = SudukoGUI(test)

# test.printBoard()
# test.setSquare((8,8), 9)
# test.printBoard()


pygame.quit()
                  