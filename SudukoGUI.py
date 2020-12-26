import pygame, SudukoSolver, time
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
from PygameButton import Button
from copy import deepcopy

#Colours
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255,255,153)

#Board Dimensions
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
SQUARE_SIZE = 600/9

#Game Constants
WINDOW_SIZE = (900, 600)
FPS = 30
board_one = [
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
board_two = [
    [0,4,0,8,0,5,2,0,0],
    [0,2,0,0,4,0,0,5,0],
    [5,0,0,0,0,0,0,0,4],
    [0,9,0,0,0,3,1,2,0],
    [1,0,6,0,7,8,0,0,3],
    [3,7,0,9,0,4,0,8,0],
    [0,0,0,0,0,6,7,0,0],
    [0,0,8,3,5,9,0,1,0],
    [0,1,9,0,0,7,6,0,0]
]

board_three = [
    [9,8,0,0,0,0,6,0,2],
    [0,0,7,0,4,0,0,0,0],
    [0,1,0,0,0,0,0,0,9],
    [5,6,0,4,0,0,0,0,0],
    [0,0,0,0,0,1,7,0,0],
    [0,0,8,0,6,0,4,1,0],
    [0,0,2,0,0,0,1,0,0],
    [0,4,5,8,0,0,0,0,6],
    [0,0,0,0,0,7,2,0,0]
]

board_custom = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
SUDUKO_BOARDS = [board_one, board_two, board_three, board_custom]

#GUI for Suduko game
class SudukoGUI():
    def __init__(self):
        pygame.init()
        self.running = True
        self.board = None
        self.buttons = []
        self.font =  pygame.font.SysFont("comicsans", 40)
        self.title_font = pygame.font.SysFont("helvetica", 100)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.fps_limit = pygame.time.Clock()
        self.game_status = "Not solved"

        #Current square being manipulated
        self.selected = None
        self.creating = False

        #Numbers not yet finalized
        self.sketches = dict()

        #Stats
        self.errors = 0
        self.hints = 3

    def title_screen(self):
        self.board = None
        board_select_y = 200
        button_gap = 30
        self.buttons = [
            Button((150, board_select_y), 180, 100, WHITE, "Board 1", 0, lambda: self.set_board(0)),
            Button((150 + 180 + button_gap, board_select_y), 180, 100, WHITE, "Board 2", 0, lambda: self.set_board(1)),
            Button((150 + (180 + button_gap) * 2, board_select_y), 180, 100, WHITE, "Board 3", 0, lambda: self.set_board(2)),
            Button((150, 300 + button_gap), 600, 100, WHITE, "Custom Board", 0, lambda: self.set_board(3)),
            Button((150, 400 + 2*(button_gap)), 600, 100, WHITE, "Start", 0, self.start_game)
        ]

        while self.running:
            self.fps_limit.tick(FPS)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == MOUSEMOTION:
                    #Button text bigger when moused over
                    for btn in self.buttons:
                        if btn.mouseHover(pos):
                            btn.font = pygame.font.SysFont("comicsans", 45)
                        else:
                            btn.font= pygame.font.SysFont("comicsans", 40)
                if event.type == MOUSEBUTTONDOWN:
                    for btn in self.buttons:
                        if btn.mouseHover(pos):
                            btn.click()
                            #Board selected will be highlighted yellow
                            for clicked in self.buttons:
                                if clicked == btn and btn.text!="Start":
                                    clicked.colour = YELLOW
                                else:
                                    clicked.colour = WHITE                    
            self.draw_title_screen()

    def draw_title_screen(self):
        self.screen.fill(BLACK)
        title = self.title_font.render("Suduko Solver!", True, WHITE)
        self.screen.blit(title, (WINDOW_SIZE[0]/2-title.get_width()/2, (WINDOW_SIZE[1]/2-title.get_height()/2)-200))
        self.draw_buttons()
        pygame.display.update()

    def set_board(self, board_index):
        self.board = SUDUKO_BOARDS[board_index]

    def solve_board(self):
        self.sketches = dict()
        self.board = self.solution
        self.selected = None

    def give_hint(self):
        if self.selected != None and self.hints > 0:
            self.hints-=1
            self.sketches.pop(self.selected, None)
            self.board[self.selected[0]][self.selected[1]] = self.solution[self.selected[0]][self.selected[1]]
            self.selected = None
        elif self.hints == 0:
            self.game_status = "No hints left"


    #Draws Suduko board
    def draw_board(self):
        self.screen.fill(WHITE)
        thicc = 1
        length = 600
        for x in range(len(self.board)+1):
            #Thicker lines for boxes
            if(x%3 == 0 and x!= 0):
                thicc = 3
                length = 600
            else:
                thicc = 1
                length = 600
            pygame.draw.line(self.screen, BLACK,(0, x*SQUARE_SIZE), (length, x*SQUARE_SIZE),thicc)

        for x in range(len(self.board[0])+1):
            if(x % 3 == 0 and x!= 0):
                thicc = 3
            else:
                thicc = 1
            pygame.draw.line(self.screen, BLACK, (x*SQUARE_SIZE, 0), (x*SQUARE_SIZE, 600), thicc)

        pygame.draw.rect(self.screen, BLACK, (620, 360, 260, 240), 2)
        pygame.draw.line(self.screen, BLACK, (620, 480), (880, 480), 2)
        
    #Draws all numbers inside squares
    def fill_squares(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col] != 0):
                    number = self.font.render(str(self.board[row][col]), True, BLACK)
                    #To center numbers, top left will be middle of grid square minus
                    #half of number with
                    xPos = (SQUARE_SIZE*col)+ (SQUARE_SIZE/2 - number.get_width()/2)
                    yPos = (SQUARE_SIZE *row) + (SQUARE_SIZE/2 - number.get_height()/2)
                    self.screen.blit(number, (xPos, yPos))
        
        #Draws numbers that are not finalized
        for sketchedNum in self.sketches:
            number = self.font.render(str(self.sketches[sketchedNum]), True, (128,128,128))
            xPos = (SQUARE_SIZE* sketchedNum[1] )+ (SQUARE_SIZE/2 - number.get_width()/2)
            yPos = (SQUARE_SIZE *sketchedNum[0]) + (SQUARE_SIZE/2 - number.get_height()/2)
            self.screen.blit(number, (xPos, yPos))

    #Draws yellow highlight over clicked square
    def draw_selected(self):
        if self.selected != None:
            highlight = pygame.Surface((BOARD_WIDTH/9-1, BOARD_HEIGHT/9-1))
            highlight.set_alpha(128)
            highlight.fill((255,255,153))
            xPos = (self.selected[1] * SQUARE_SIZE)+1
            yPos = (self.selected[0] * SQUARE_SIZE)+1
            self.screen.blit(highlight, (xPos, yPos))

    #Draws all buttons to screen
    def draw_buttons(self):
        for btn in self.buttons:
            btn.drawButton(self.screen)

    #Updates clock to screen
    def draw_stats(self, start_time):
        currentTime = round(time.time()-start_time)
        seconds = currentTime % 60
        minutes = currentTime // 60
        text = str(minutes) + " : " + str(seconds)
        clock = self.font.render(text, True, BLACK)
        xPos = (600+150)- (clock.get_width()/2)
        yPos = (450)- (clock.get_height()/2)
        self.screen.blit(clock, (xPos, yPos))

        errors = self.font.render("Errors: " + str(self.errors), True, BLACK)
        self.screen.blit(errors, (750-errors.get_width()/2, yPos-clock.get_height()))

        hints = self.font.render("Hints Left: " + str(self.hints), True, BLACK)
        self.screen.blit(hints, (750-hints.get_width()/2, yPos-clock.get_height()-errors.get_height()))

        status = self.font.render(self.game_status, True, BLACK)
        self.screen.blit(status, (750-status.get_width()/2, 540-status.get_height()/2))

    #Changes square currently selected
    def set_select(self, pos):
        if(self.selected != pos and self.board[pos[0]][pos[1]] == 0):
            self.selected = pos  

    #Input for a square is tried against solution, stays if correct else error is counted and
    #square is reset
    def try_square(self, num):
        if self.sketches.get(self.selected) != None:
            attempt = self.sketches.pop(self.selected)
            #If attempt matches solution, set board position to attempt
            if(attempt == self.solution[self.selected[0]][self.selected[1]]):
                self.game_status = "Correct"
                self.board[self.selected[0]][self.selected[1]] = attempt
                self.selected = None
            else:
                self.game_status = "Incorrect"
                self.errors +=1        

    def draw_game_screen(self, start_time):
        self.draw_board()
        self.fill_squares()
        self.draw_selected()
        self.draw_buttons()
        if not self.creating:
            self.draw_stats(start_time)
        pygame.display.update()
        
    #User input taken before number is checked against solution    
    def sketch_num(self, num):
        row = self.selected[0]
        col = self.selected[1]
        if(self.board[row][col] == 0):
            number = self.font.render(str(num), False, (128,128,128))
            xPos = (SQUARE_SIZE*col)+ (SQUARE_SIZE/2 - number.get_width()/2)
            yPos = (SQUARE_SIZE *row) + (SQUARE_SIZE/2 - number.get_height()/2)
            self.screen.blit(number, (xPos, yPos))
            self.sketches.update({(row, col) : num})

    def clear_sketch(self):
        self.sketches.pop(self.selected, None)               

    def create_board(self, board):
        self.board = board

    def stop(self):
        self.creating = False
    def start_game(self):
        #Board must be selected
        if self.board!= None:             
            self.buttons = [
                Button((620, 0), 260, 100, BLACK, "Solve", 1, self.solve_board),
                Button((620, 120), 260, 100, BLACK, "Hint", 1, self.give_hint),
                Button((620, 240), 260, 100, BLACK, "Menu", 1, self.title_screen)
            ]
            start_time = time.time()
            self.game_status = "Not solved"
            self.solution = deepcopy(self.board)
            SudukoSolver.solve_board(self.solution)
            while self.running :
                num = None
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        #Start button
                        for btn in self.buttons:
                            #If mouse over button, enlarge font
                            if btn.mouseHover(pos):
                                btn.font = pygame.font.SysFont("comicsans", 45)
                            else:
                                btn.font= pygame.font.SysFont("comicsans", 40)
                    elif event.type == pygame.KEYDOWN and self.selected!= None:
                        #Try sketch against board solution
                        if event.key == pygame.K_RETURN:
                            self.try_square(self.sketches.get(self.selected))
                        #Delete sketch
                        elif event.key == pygame.K_DELETE:
                            self.clear_sketch()
                        #Get user sketch
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
                        #Draw user sketch
                        if num != None:
                            self.sketch_num(num)                        

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        #If mouse is on the board, get square selected
                        if pos[0] <= 600:
                            row = int(pos[1] // (BOARD_HEIGHT/9))
                            col = int(pos[0] // (BOARD_WIDTH/9))                    
                            self.set_select((row,col))
                        #Check if a button was pressed 
                        else:
                            for btn in self.buttons:
                                if btn.mouseHover(pos):
                                    btn.click()

                if self.board == self.solution:
                    self.game_status = "Solved"
                self.draw_game_screen(start_time)

gameTest = SudukoGUI()
gameTest.title_screen()