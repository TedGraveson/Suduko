'''board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]'''

board = [
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

#prints the state of the board
def printBoard(board):
    
    for row in range(len(board)):

        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - -')
        
        for col in range(len(board[0])):
            
            if col % 3 == 0 and col != 0:
                print('|', end=' ')
                
            if col == 8:
                print (board[row][col])
                
            else:
                print(board[row][col], end=' ')

#find the next empty space on the board
def emptySpace(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return(row,col) #returns tuple

    return None

                         

#checks if a move is valid    
def checkMove(pos, num, board):

    #row
    for col in range(len(board[0])):
        if board[pos[0]][col] == num:
            return False
    #col
    for y in range(len(board)):
        if board[y][pos[1]] == num:
            return False

    #counts from top left index of box that number is being placed in
    boxRow = (pos[0] // 3)*3 
    boxCol = (pos[1] // 3)*3
    
    #box
    for row in range(boxRow, boxRow+3):
        for col in range(boxCol, boxCol+3):
            if board[row][col] == num:
                return False

    return True
    
def solve(board):

    solveSpace = emptySpace(board)

    #base case
    if solveSpace == None:
        return True
    else:
        row = solveSpace[0]
        col = solveSpace[1]

        for num in range(1,10):
            #if number is valid, recursively fill board
            if checkMove(solveSpace, num, board) == True:
                board[row][col] = num
                solve(board)
                #if board solved, leave it as it
                if solve(board) == True:
                    return True
            #if no solutions possible down this branch, revert back to root
            board[row][col]=0

                
            
            
        

        
        
                

printBoard(board)
print(emptySpace(board))
print(checkMove((0,2), 3, board))
solve(board)
printBoard(board)

