import pygame
import SudukoSolver
from MyButtonClass import Button
from copy import deepcopy

#Colours
white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)


#GUI for Suduko game
class SudukoGUI():
    def __init__(self, suduko):

        pygame.init()
        self.running = True
        self.board = suduko

        #Window dimensions
        self.windowSize = (900, 600)
        self.boardWidth = 600
        self.boardHeight = 600
        self.squareSize = 600/9


        self.font =  pygame.font.SysFont("comicsans", 40)
        self.screen = pygame.display.set_mode(self.windowSize)

        #Current square being manipulated
        self.selected = (0,0)

        #Numbers not yet finalized
        self.sketches = dict()

        self.errors = 0
        self.buttons = [
            Button((700, 10), 100, 100, red, "Solve"),
            Button((700, 110), 100 ,100, red, "Another")
        ]
        self.clock = pygame.time.Clock()

        #Solution to Suduko board
        self.solution = deepcopy(suduko)
        SudukoSolver.solve(self.solution)

        self.drawBoard() 
        self.updateBoard()     
               
        self.startGame()

    
    def drawBoard(self):
        self.screen.fill(white)
        squareSize = self.boardWidth/9
        thicc = 1
        length = 600
        for x in range(len(self.board)+1):
            #Thicker lines for boxes
            if(x%3 == 0 and x!= 0):
                thicc = 3
                length = 900
            else:
                thicc = 1
                length = 600
            pygame.draw.line(self.screen, black,(0, x*squareSize), (length, x*squareSize),thicc)

        for x in range(len(self.board[0])+1):
            if(x % 3 == 0 and x!= 0):
                thicc = 3
            else:
                thicc = 1
            pygame.draw.line(self.screen, black, (x*squareSize, 0), (x*squareSize, 600), thicc)
        
        font = pygame.font.SysFont("comicsans", 40)

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col] != 0):
                    # print(str(row) + ", " + str(col))
                    txt = font.render(str(self.board[row][col]), True, black)
                    # self.screen.blit(txt, ((gap * row),(gap*col) ))
                    #To center numbers, top left will be middle of grid square minus
                    #half of number with
                    xPos = (squareSize*col)+ (squareSize/2 - txt.get_width()/2)
                    yPos = (squareSize *row) + (squareSize/2 - txt.get_height()/2)
                    self.screen.blit(txt, (xPos, yPos))
        
        for sketchedNum in self.sketches:
            text = self.font.render(str(self.sketches[sketchedNum]), True, (128,128,128))
            xPos = (self.squareSize* sketchedNum[1] )+ (self.squareSize/2 - text.get_width()/2)
            yPos = (self.squareSize *sketchedNum[0]) + (self.squareSize/2 - text.get_height()/2)
            self.screen.blit(text, (xPos, yPos))

        
        self.drawSelected()
        self.drawButtons()

    def selectSquare(self, pos):
        if(self.selected != pos):
            self.selected = pos
            
        
    def drawSelected(self):
        highlight = pygame.Surface((self.boardWidth/9 -1, self.boardHeight/9-1))
        highlight.set_alpha(128)
        highlight.fill((255,255,153))
        xPos = (self.selected[1] * self.squareSize)+1
        yPos = (self.selected[0] * self.squareSize)+1
        self.screen.blit(highlight, (xPos, yPos))

    def drawButtons(self):
        for btn in self.buttons:
            btn.drawButton(self.screen)

    def drawClock(self):
        pass


    def changeNum(self, num):
        print("Changing array: " + str(self.selected) + " to " + str(num))
        attempt = self.sketches.pop(self.selected)
        #If number matches solution
        if(attempt == self.solution[self.selected[0]][self.selected[1]]):
            self.board[self.selected[0]][self.selected[1]] = attempt
        else:
            self.errors +=1
            print("wrong")


        
        print(self.board)

    def updateBoard(self):
        pygame.display.update()
        self.drawBoard()
        self.selectSquare(self.selected)
        
    def sketchNum(self, num):
        row = self.selected[0]
        col = self.selected[1]
        print("Sketch " + str(row) + str(col))
        if(self.board[row][col] == 0):
            text = self.font.render(str(num), False, (128,128,128))
            xPos = (self.squareSize*col)+ (self.squareSize/2 - text.get_width()/2)
            yPos = (self.squareSize *row) + (self.squareSize/2 - text.get_height()/2)
            self.screen.blit(text, (xPos, yPos))
            self.sketches.update({(row, col) : num})



    def testLoop(self):
        self.updateBoard()
        self.updateBoard()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
    def startGame(self):
        while self.running :
            num = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.sketches[self.selected]!= None:
                            self.changeNum(self.sketches[self.selected])
                    elif event.key == pygame.K_1:
                        num = 1
                    elif event.key == pygame.K_2:
                        num = 2
                    elif event.key == pygame.K_3:
                        num = 3
                    elif event.key == pygame.K_4:
                        num = 4
                    elif event.key == pygame.K_5:
                        num = 5
                    elif event.key == pygame.K_6:
                        num = 6    
                    elif event.key == pygame.K_7:
                        num = 7
                    elif event.key == pygame.K_8:
                        num = 8
                    elif event.key == pygame.K_9:
                        num = 9
                    if num != None:
                        self.sketchNum(num)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 600:
                        row = int(pos[1] // (self.boardHeight/9))
                        col = int(pos[0] // (self.boardWidth/9)) 
                        print(str(row) + str(col))                       
                        self.selectSquare((row,col))
                    else:
                        for btn in self.buttons:
                            if btn.mouseHover(pos):
                                self.board = self.solution

            self.updateBoard()         
            

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


gameTest = SudukoGUI(arr)

#def drawSquare(self, gridSquare):
    #     #Number to be drawn
    #     square = self.font.render(str(gridSquare.getNum()), False, (0,0,0))
    #     boardWidth = self.windowSize[0]-(self.windowSize[0]/3)
    #     boardHeight = self.windowSize[1]
    #     row = boardWidth/9 * gridSquare.getPos()[0]
    #     col = boardHeight/9 * gridSquare.getPos()[1]
    #     self.screen.blit(square, (row, col))

    # def showFocus(self):
    #     highlight = pygame.Surface((self.boardWidth/9, self.boardHeight/9))
    #     highlight.set_alpha(128)
    #     highlight.fill((255,255,153))
    #     rowPos = self.boardWidth/9 * self.selected[0]
    #     colPos = self.boardHeight/9* self.selected[1]
    #     self.screen.blit(highlight, (rowPos+1,colPos+1))