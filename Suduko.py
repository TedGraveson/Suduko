import pygame
from pygame.constants import RESIZABLE


boardImg = pygame.image.load("SudokuBoard900.jpg")
boardImg = pygame.transform.scale(boardImg, (600, 600))

white = (255,255,255)

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

    def setSelect(self, state):
        self.selected = state

    def __str__(self):
        return str(self.num)

class Suduko():
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

    def selectSquare(self, pos):
        self.getSquare(pos).setSelect(True)



class SudukoGUI():
    def __init__(self, suduko):
        pygame.init()
        self.running = True
        self.board = suduko
        self.windowSize = (900, 600)
        self.boardWidth = 600
        self.boardHeight = 600
        self.screen = pygame.display.set_mode(self.windowSize)
        self.screen.blit(boardImg, (0,0))
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.focusSquare = (0,0)
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
        boardWidth = self.windowSize[0]-(self.windowSize[0]/3)
        boardHeight = self.windowSize[1]
        xPos = boardWidth/9 * gridSquare.getPos()[1]
        yPos = boardHeight/9 * gridSquare.getPos()[0]
        self.screen.blit(square, (yPos, xPos))
        pygame.display.update()
        

    def startGame(self):
        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.board.setSquare(self.focusSquare, pygame.key.name(event.key))
                    self.drawBoard()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 600:
                        col = int(pos[0] // (self.boardWidth/9))
                        row = int(pos[1] // (self.boardHeight/9))
                        self.drawSquare(self.board.getSquare((row,col)))
                        self.board.selectSquare((row,col))
                        self.focusSquare = (row,col)
                        

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

    



test = Suduko(arr)
suduko = SudukoGUI(test)

# test.printBoard()
# test.setSquare((8,8), 9)
# test.printBoard()


pygame.quit()
                  

