import pygame
import os


boardImg = pygame.image.load("SudokuBoard900.jpg")
class GridSquare():
    def __init__(self, pos, num):
        self.row = pos[0]
        self.col = pos[1]
        self.num = num
        self.selected = False

    def getPos(self):
        return (self.row, self.col)

    def getNum(self):
        return self.num

    def setNum(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

class Board():
    def __init__(self):
        self.boardState = []
        for row in range(9):
            rowToAdd = []
            for col in range(9):
                rowToAdd.append(GridSquare((col, row), 8))
            self.boardState.append(rowToAdd)


    def printBoard(self):
        for row in self.boardState:
            for pos in row:
                print(pos, end=' ') 
            print()
        print()

    #Addressed from left right 
    def setPos(self, pos, num) :
        x = pos[1]-1
        y = pos[0]-1
        self.boardState[y][x].setNum(num)

    def getSquare(self, pos):
        return self.boardState[pos[0]][pos[1]]


class Suduko():
    def __init__(self, board):
        pygame.init()
        self.running = True
        self.board = board
        self.windowSize = self.width, self.height = (900, 900)
        self.screen = pygame.display.set_mode(self.windowSize)
        self.screen.blit(boardImg, (0,0))
        self.font = pygame.font.Font('freesansbold.ttf', 100)
        pygame.display.update()
        self.startGame()

    
    def updateBoard(self):
        for col in range(9):
            for row in range(9):
                self.drawPos(self.board.getSquare((row, col)))

    def drawPos(self, gridSquare):
        print(gridSquare.getNum)
        square = self.font.render(str(gridSquare.getNum()), False, (0,0,0))
        xPos = gridSquare.getPos()[0] *100 + 25
        yPos = gridSquare.getPos()[1] *100 + 10
        print(xPos)
        print(yPos)
        self.screen.blit(square, (xPos, yPos))
        pygame.display.update()

    def startGame(self):
        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == py
                    self.updateBoard()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if(pos[0] < 100):
                        self.v
                    elif(pos[0] < 200):


    



test = Board()
test.printBoard()
test.setPos((9,9), 9)
test.printBoard()


game = Suduko(test)
pygame.quit()
                  