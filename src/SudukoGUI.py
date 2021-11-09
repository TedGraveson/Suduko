import pygame, SudukoSolver, time
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
from PygameButton import Button
from copy import deepcopy
from Constants import *
#Running the GUI

#GUI for Suduko game
class SudukoGUI():
    def __init__(self):
        pygame.init()
        self.running = True
        #Current board selected
        self.board = None
        #Buttons currently displayed
        self.buttons = []

        #Pygame values
        self.font =  pygame.font.SysFont("comicsans", 40)
        self.title_font = pygame.font.SysFont("helvetica", 100)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.fps_limit = pygame.time.Clock()

        #Game message
        self.game_status = "Not solved"

        #Current square being manipulated
        self.selected = None

        #Numbers not yet finalized, inputted by user
        self.sketches = dict()

        #Stats
        self.errors = 0
        self.hints = 3
        self.clock_time = ""

    
    #Changes board to be displayed
    def set_board(self, board_index):
        self.board = SUDUKO_BOARDS[board_index]

    #Shows the full solution to a given board
    def solve_board(self):
        self.sketches = dict()
        self.board = self.solution
        self.selected = None

    #Currently selected square is solved
    def give_hint(self):
        #Check if square is selected and that user has hints left
        if self.selected != None and self.hints > 0:
            self.hints-=1
            #Remove any sketeches for selected square
            self.sketches.pop(self.selected, None)
            
            self.board[self.selected[0]][self.selected[1]] = self.solution[self.selected[0]][self.selected[1]]
            self.selected = None
        elif self.hints == 0:
            self.game_status = "No hints left"


    #Draws Suduko board
    def draw_board(self):
        self.screen.fill(WHITE)
        thickness = 1
        length = 600
        #Draw horizontal lines
        for x in range(10):
            #Thicker lines for boxes
            if(x%3 == 0 and x!= 0):
                thickness = 3
            else:
                thickness = 1
            pygame.draw.line(self.screen, BLACK,(0, x*SQUARE_SIZE), (length, x*SQUARE_SIZE),thickness)

        #Draw vertical lines
        for x in range(10):
            if(x % 3 == 0 and x!= 0):
                thickness = 3
            else:
                thickness = 1
            pygame.draw.line(self.screen, BLACK, (x*SQUARE_SIZE, 0), (x*SQUARE_SIZE, 600), thickness)


        #Score divider
        # pygame.draw.line(self.screen, BLACK, (620, 580), (880, 580), 2)
        
    #Draws all numbers inside squares
    def fill_squares(self):
        if self.board != None:
            for row in range(9):
                for col in range(9):
                    #Draw all finalized numbers
                    if(self.board[row][col] != 0):
                        number = self.font.render(str(self.board[row][col]), True, BLACK)
                        #To center numbers, top left will be middle of grid square minus
                        #half of number with
                        x_pos = (SQUARE_SIZE*col)+ (SQUARE_SIZE/2 - number.get_width()/2)
                        y_pos = (SQUARE_SIZE *row) + (SQUARE_SIZE/2 - number.get_height()/2)
                        self.screen.blit(number, (x_pos, y_pos))
            
            #Draws numbers that are not finalized, getting position held in self.sketches
            for sketched_num in self.sketches:
                number = self.font.render(str(self.sketches[sketched_num]), True, (128,128,128))
                x_pos = (SQUARE_SIZE* sketched_num[1] )+ (SQUARE_SIZE/2 - number.get_width()/2)
                y_pos = (SQUARE_SIZE *sketched_num[0]) + (SQUARE_SIZE/2 - number.get_height()/2)
                self.screen.blit(number, (x_pos, y_pos))

    #Draws yellow highlight over clicked square
    def draw_selected(self):
        if self.selected != None:
            highlight = pygame.Surface((BOARD_WIDTH/9-1, BOARD_HEIGHT/9-1))
            highlight.set_alpha(128)
            highlight.fill((255,255,153))
            x_pos = (self.selected[1] * SQUARE_SIZE)+1
            y_pos = (self.selected[0] * SQUARE_SIZE)+1
            self.screen.blit(highlight, (x_pos, y_pos))

    #Draws all buttons to screen
    def draw_buttons(self):
        for btn in self.buttons:
            btn.draw_button(self.screen)

    #Updates all stats
    def draw_stats(self, start_time):
        if self.game_status != "Solved":
            #Formatting time elapsed
            current_time = round(time.time()-start_time)
            seconds = current_time % 60
            minutes = current_time // 60
            self.clock_time =  str(minutes) + " : " + str(seconds)
        
        #Draw clock
        clock = self.font.render(self.clock_time, True, BLACK)
        x_pos = (600+150)- (clock.get_width()/2)
        y_pos = (500)- (clock.get_height()/2)
        self.screen.blit(clock, (x_pos, y_pos))

        #Draw errors
        errors = self.font.render("Errors: " + str(self.errors), True, BLACK)
        self.screen.blit(errors, (750-errors.get_width()/2, y_pos-clock.get_height()))

        #Draw remaining hints
        hints = self.font.render("Hints Left: " + str(self.hints), True, BLACK)
        self.screen.blit(hints, (750-hints.get_width()/2, y_pos-clock.get_height()-errors.get_height()))

        #Draw current game status
        status = self.font.render(self.game_status, True, BLACK)
        self.screen.blit(status, (750-status.get_width()/2, 520))

    #Changes square currently selected
    def set_select(self, pos):
        if(self.selected != pos and self.board[pos[0]][pos[1]] == 0):
            self.selected = pos  

    #Sketch for a square is tried against solution, confirms if correct else error is counted and
    #square is reset
    def try_square(self):
        if self.sketches.get(self.selected) != None:
            attempt = self.sketches.pop(self.selected)
            #If current sketch matches solution, set board position to that sketched number
            if(attempt == self.solution[self.selected[0]][self.selected[1]]):
                self.game_status = "Correct"
                self.board[self.selected[0]][self.selected[1]] = attempt
                self.selected = None
            else:
                self.game_status = "Incorrect"
                self.errors +=1        

    
        
    #User tentative answer for selected square is stored
    def sketch_num(self, num):
        row = self.selected[0]
        col = self.selected[1]
        if(self.board[row][col] == 0):
            self.sketches.update({(row, col) : num})

    def clear_sketch(self):
        self.sketches.pop(self.selected, None)               

    #Method for quit button
    def stop_game(self):
        self.running= False
    
    #Title screen for the game
    def title_screen(self):
        self.board = None
        board_button_y_pos = 200
        #Change in x position from previous board button
        button_gap = 210

        self.buttons = [
            #Board selecting buttons
            Button((150, board_button_y_pos), 180, 100, YELLOW, "Board 1", 0, lambda: self.set_board(0)),
            Button((150 + button_gap, board_button_y_pos), 180, 100, WHITE, "Board 2", 0, lambda: self.set_board(1)),
            Button((150 + button_gap * 2, board_button_y_pos), 180, 100, WHITE, "Board 3", 0, lambda: self.set_board(2)),

            #Start and quit buttons
            Button((150, 300 + 30), 600, 100, WHITE, "Start", 0, self.start_game),
            Button((150, 400 + 2 * 30), 600, 100, WHITE, "Quit", 0, self.stop_game )
        ]

        #First board is default
        self.buttons[0].click()

        #Title screen running loop
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
                        #If button is clicked, perform function given to button
                        if btn.mouseHover(pos):
                            btn.click()
                            #Board selected will be highlighted yellow
                            for clicked in self.buttons:
                                if clicked == btn and btn.text!="Start":
                                    clicked.colour = YELLOW
                                else:
                                    clicked.colour = WHITE                    
            self.draw_title_screen()

    #Updates title screen elements
    def draw_title_screen(self):
        self.screen.fill(BLACK)
        title = self.title_font.render("Suduko Solver!", True, WHITE)
        self.screen.blit(title, (WINDOW_SIZE[0]/2-title.get_width()/2, (WINDOW_SIZE[1]/2-title.get_height()/2)-200))
        self.draw_buttons()
        pygame.display.update()

    def start_game(self):
        #Board must be selected
        if self.board!= None:             
            self.buttons = [
                Button((620, 0), 260, 100, BLACK, "Solve", 1, self.solve_board),
                Button((620, 120), 260, 100, BLACK, "Hint", 1, self.give_hint),
                Button((620, 240), 260, 100, BLACK, "Menu", 1, self.title_screen)
            ]
            start_time = time.time()
            self.selected = None
            self.sketches = dict()
            self.game_status = "Not solved"
            self.solution = deepcopy(self.board)
            SudukoSolver.solve_board(self.solution)

            #Main game loop
            while self.running :
                num = None
                #Event loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        for btn in self.buttons:
                            #If mouse over button, enlarge font
                            if btn.mouseHover(pos):
                                btn.font = pygame.font.SysFont("comicsans", 45)
                            else:
                                btn.font= pygame.font.SysFont("comicsans", 40)
                    elif event.type == pygame.KEYDOWN and self.selected!= None:
                        #Try sketch against board solution
                        if event.key == pygame.K_RETURN:
                            self.try_square()
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

    #Updates game screen state
    def draw_game_screen(self, start_time):
        self.draw_board()
        self.fill_squares()
        self.draw_selected()
        self.draw_buttons()
        self.draw_stats(start_time)
        pygame.display.update()

game = SudukoGUI()
game.title_screen()