import pygame
import Suduko

class SudukoGUI():
    def __init__(self, suduko):
        pygame.init()
        self.running = True
        self.board = suduko
        self.windowSize = (900, 600)
        self.boardWidth = 600
        self.boardHeight = 600
        self.screen = pygame.display.set_mode(self.windowSize)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.focusSquare = (0,0)
        self.drawBoard()

    
    def drawBoard(self):
        self.screen.blit(boardImg, (0,0))
        for col in range(9):
            for row in range(9):
                if self.board.getSquare((row,col)).getNum() != 0:
                    self.drawSquare(self.board.getSquare((row, col)))
        self.showFocus()
        pygame.display.update()


    def drawSquare(self, gridSquare):
        #Number to be drawn
        square = self.font.render(str(gridSquare.getNum()), False, (0,0,0))
        boardWidth = self.windowSize[0]-(self.windowSize[0]/3)
        boardHeight = self.windowSize[1]
        row = boardWidth/9 * gridSquare.getPos()[0]
        col = boardHeight/9 * gridSquare.getPos()[1]
        self.screen.blit(square, (row, col))

    def showFocus(self):
        highlight = pygame.Surface((self.boardWidth/9, self.boardHeight/9))
        highlight.set_alpha(128)
        highlight.fill((255,255,153))
        rowPos = self.boardWidth/9 * self.focusSquare[0]
        colPos = self.boardHeight/9* self.focusSquare[1]
        self.screen.blit(highlight, (rowPos+1,colPos+1))

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
                        if(self.board.checkMove(self.focusSquare, num)):
                            self.board.setSquare(self.focusSquare, num)                
                            self.drawBoard()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 600:
                        col = int(pos[1] // (self.boardWidth/9))
                        row = int(pos[0] // (self.boardHeight/9))
                        self.board.selectSquare((row,col))
                        self.focusSquare = (row,col)
                        self.drawBoard()
                        

                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((self.screen.get_width(),self.screen.get_height()), pygame.RESIZABLE)
                    self.screen.blit(boardImg, (0,0))
            pygame.display.update()    