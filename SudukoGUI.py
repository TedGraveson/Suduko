import pygame
import Suduko

white = (255,255,255)
black = (0, 0, 0)

class SudukoGUI():
    def __init__(self, suduko):
        pygame.init()
        self.running = True
        self.board = suduko
        self.windowSize = (900, 600)
        self.boardWidth = 600
        self.boardHeight = 600
        self.squareSize = self.boardWidth/9
        self.font =  pygame.font.SysFont("comicsans", 40)
        self.screen = pygame.display.set_mode(self.windowSize)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.selected = None
        self.drawBoard() 
        self.updateBoard()       
        self.startGame()

    
    def drawBoard(self):
        self.screen.fill(white)
        squareSize = self.boardWidth/9
        thicc = 1
        for x in range(len(self.board)+1):
            #Thicker lines for boxes
            if(x%3 == 0 and x!= 0):
                thicc = 3
            else:
                thicc = 1
            print("yo")
            pygame.draw.line(self.screen, black,(0, x*squareSize), (600, x*squareSize),thicc)

        for x in range(len(self.board[0])+1):
            if(x % 3 == 0 and x!= 0):
                thicc = 3
            else:
                thicc = 1
            pygame.draw.line(self.screen, black, (x*squareSize, 0), (x*squareSize, 600), thicc)
        
        font = pygame.font.SysFont("comicsans", 40)

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                txt = font.render(str(self.board[row][col]), False, black)
                # self.screen.blit(txt, ((gap * row),(gap*col) ))
                #To center numbers, top left will be middle of grid square minus
                #half of number with
                xPos = (squareSize*row)+ (squareSize/2 - txt.get_width()/2)
                yPos = (squareSize *col) + (squareSize/2 - txt.get_height()/2)
                self.screen.blit(txt, (xPos, yPos))


    def selectSquare(self, pos):
        if(self.selected != pos):
            self.drawBoard()
            self.selected = pos
            highlight = pygame.Surface((self.boardWidth/9 -1, self.boardHeight/9-1))
            highlight.set_alpha(128)
            highlight.fill((255,255,153))
            xPos = (self.selected[0] * self.squareSize)+1
            yPos = (self.selected[1] * self.squareSize)+1
            self.screen.blit(highlight, (xPos, yPos))

    def setSelected(self, num):
        self.board[self.selected[0]][self.selected[1]] = num

    def updateBoard(self):
        pygame.display.update()
        self.drawBoard()
        

    def startGame(self):
        while self.running :
            num = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
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
                        self.setSelected(num)
                        self.updateBoard()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 600:
                        col = int(pos[1] // (self.boardWidth/9))
                        row = int(pos[0] // (self.boardHeight/9))
                        self.selectSquare((row,col))
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