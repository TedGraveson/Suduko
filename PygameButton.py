import pygame

class Button():
    def __init__(self, pos, width, height, colour, text = "", filled = 0, action = None):
        self.pos = pos
        self.xPos = pos[0]
        self.yPos = pos[1]

        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.font = pygame.font.SysFont("comicsans", 40)
        self.filled = filled
        
        #Function to be passed
        self.action = action


    def drawButton(self, screen):
        pygame.draw.rect(screen, self.colour, (self.xPos, self.yPos, self.width, self.height), self.filled)
        if self.text != "":
            buttonLabel = self.font.render(self.text, True, (0,0,0))
            xPos = (self.xPos + self.width/2)-(buttonLabel.get_width()/2)
            yPos = (self.yPos + self.height/2) - (buttonLabel.get_height()/2)
            screen.blit(buttonLabel, (xPos, yPos))
        


    def mouseHover(self, pos):
        if pos[0] > self.xPos and pos[0] < self.xPos+ self.width:
            if pos[1] > self.yPos and pos[1] < self.yPos + self.height:
                return True
        return False
    
    def click(self):
        if self.action != None:
            self.action()
