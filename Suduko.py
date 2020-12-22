# import pygame
# from pygame.constants import RESIZABLE


# boardImg = pygame.image.load("SudokuBoard900.jpg")
# boardImg = pygame.transform.scale(boardImg, (600, 600))

# white = (255,255,255)

# class GridSquare():
#     def __init__(self, pos, num):
#         self.pos = pos
#         self.num = num
#         self.selected = False

#     def getPos(self):
#         return self.pos

#     def getNum(self):
#         return self.num

#     def setNum(self, num):
#         self.num = num

#     def setSelect(self, state):
#         self.selected = state

#     def __str__(self):
#         return str(self.num)

# class Suduko():
#     def __init__(self, board):
#         self.board = []
#         for row in range(len(board)):
#             rowToAdd = []
#             for col in range(len(board[0])):
#                 rowToAdd.append(GridSquare((row, col),board[row][col]))
#             self.board.append(rowToAdd)


#     def printBoard(self):
#         for row in self.board:
#             for pos in row:
#                 print(pos, end=' ') 
#             print()
#         print()

#     #Addressed from left right 
#     def setSquare(self, pos, num) :
#         self.board[pos[0]][pos[1]].setNum(num)

#     def getSquare(self, pos):
#         return self.board[pos[0]][pos[1]]


#     def selectSquare(self, pos):
#         self.getSquare(pos).setSelect(True)

#     #Finds next empty spot in board
#     def nextEmptySpace(self):
#         for row in range(len(self.board)):
#             for col in range(len(self.board[0])):
#                 if self.board[row][col].getNum() == 0:
#                     return self.board[row][col].getSquare().getPos()
#         return None

#     def checkMove(self, pos, num):
#         moveRow = pos[0]
#         moveCol = pos[1]
#         #Check row
#         for checkCol in range(len(self.board[moveRow])):
#             if(self.board[moveRow][checkCol].getNum() == num):
#                 print("Row" + str(self.board[moveRow][checkCol].getPos()))
#                 return False

#         #Check col
#         for checkRow in range(len(self.board[moveCol])):
#             if(self.board[checkRow][moveCol].getNum() == num):
#                 print("Col" + str(self.board[checkRow][moveCol].getPos()))
#                 return False

#         #Check box
#         boxRow = (moveRow // 3) * 3
#         boxCol = (moveCol// 3) * 3

#         for checkRow in range(boxRow, boxRow+3):
#             for checkCol in range(boxCol, boxCol+3):
#                 if (self.board[checkRow][checkCol].getNum() == num):
#                     print("box" + str(self.board[checkRow][checkCol].getPos()))
#                     return False

#         return True
  


# class SudukoGUI():
#     def __init__(self, suduko):
#         pygame.init()
#         self.running = True
#         self.board = suduko
#         self.windowSize = (900, 600)
#         self.boardWidth = 600
#         self.boardHeight = 600
#         self.screen = pygame.display.set_mode(self.windowSize)
#         self.font = pygame.font.Font('freesansbold.ttf', 50)
#         self.focusSquare = (0,0)
#         self.drawBoard()
#         pygame.display.update()
#         self.startGame()

    
#     def drawBoard(self):
#         self.screen.blit(boardImg, (0,0))
#         for col in range(9):
#             for row in range(9):
#                 if self.board.getSquare((row,col)).getNum() != 0:
#                     self.drawSquare(self.board.getSquare((row, col)))
#         self.showFocus()
#         pygame.display.update()


#     def drawSquare(self, gridSquare):
#         #Number to be drawn
#         square = self.font.render(str(gridSquare.getNum()), False, (0,0,0))
#         boardWidth = self.windowSize[0]-(self.windowSize[0]/3)
#         boardHeight = self.windowSize[1]
#         row = boardWidth/9 * gridSquare.getPos()[0]
#         col = boardHeight/9 * gridSquare.getPos()[1]
#         self.screen.blit(square, (row, col))

#     def showFocus(self):
#         highlight = pygame.Surface((self.boardWidth/9, self.boardHeight/9))
#         highlight.set_alpha(128)
#         highlight.fill((255,255,153))
#         rowPos = self.boardWidth/9 * self.focusSquare[0]
#         colPos = self.boardHeight/9* self.focusSquare[1]
#         self.screen.blit(highlight, (rowPos+1,colPos+1))

#     def startGame(self):
#         while self.running :
#             num = None
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_1:
#                         num = 1
#                     elif event.key == pygame.K_2:
#                         num = 2
#                     elif event.key == pygame.K_3:
#                         num = 3
#                     elif event.key == pygame.K_4:
#                         num = 4
#                     elif event.key == pygame.K_5:
#                         num = 5
#                     elif event.key == pygame.K_6:
#                         num = 6    
#                     elif event.key == pygame.K_7:
#                         num = 7
#                     elif event.key == pygame.K_8:
#                         num = 8
#                     elif event.key == pygame.K_9:
#                         num = 9
#                     if num != None:
#                         if(self.board.checkMove(self.focusSquare, num)):
#                             self.board.setSquare(self.focusSquare, num)                
#                             self.drawBoard()
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     pos = pygame.mouse.get_pos()
#                     if pos[0] <= 600:
#                         col = int(pos[1] // (self.boardWidth/9))
#                         row = int(pos[0] // (self.boardHeight/9))
#                         self.board.selectSquare((row,col))
#                         self.focusSquare = (row,col)
#                         self.drawBoard()
                        

#                 elif event.type == pygame.VIDEORESIZE:
#                     self.screen = pygame.display.set_mode((self.screen.get_width(),self.screen.get_height()), pygame.RESIZABLE)
#                     self.screen.blit(boardImg, (0,0))
#             pygame.display.update()        


# arr = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]
    
# # class Suduko():
# #     def __init__(self, board):
# #         self.board = []
# #         for row in range(9):
# #             rowToAdd = []
# #             for col in range(9):
# #                 rowToAdd.append(board[row][col])
# #             self.board.append(rowToAdd)

    



# test = Suduko(arr)
# suduko = SudukoGUI(test)

# # test.printBoard()
# # test.setSquare((8,8), 9)
# # test.printBoard()


# pygame.quit()
                  

