import pygame
#Class for helping make interactive buttons

#Button objects to be displayed to screen
class Button():
    def __init__(self, pos, width, height, colour, text = "", filled = 0, action = None):
        self.pos = pos
        self.x_pos = pos[0]
        self.y_pos = pos[1]

        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.font = pygame.font.SysFont("comicsans", 40)

        #Rectangle drawn with filled rectangle if filled = 0, otherwise
        #specifies the width of the outline
        self.filled = filled
        
        #Function to be passed
        self.action = action

    #Button drawn to the screen
    def draw_button(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x_pos, self.y_pos, self.width, self.height), self.filled)
        #Centers text in the rectangle

        if self.text != "":
            button_label = self.font.render(self.text, True, (0,0,0))
            x = (self.x_pos + self.width/2)-(button_label.get_width()/2)
            y = (self.y_pos + self.height/2) - (button_label.get_height()/2)
            screen.blit(button_label, (x, y))
        

    #Checks if mouse is colliding with the button
    def mouseHover(self, pos):
        if pos[0] > self.x_pos and pos[0] < self.x_pos+ self.width:
            if pos[1] > self.y_pos and pos[1] < self.y_pos + self.height:
                return True
        return False
    
    #Calls the function of the button
    def click(self):
        if self.action != None:
            self.action()
