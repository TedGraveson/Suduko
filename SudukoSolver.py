#Checks if a move is valid
def check_move(board, pos, num):
    row = pos[0]
    col = pos[1]

    #Check row
    for check in board[row]:
        if check == num:
            return False
    

    #Check col
    for check in range(9):
        if board[check][col] == num:
            return False

    #Check box
    start_row = (row // 3 ) * 3
    start_col = (col // 3) *3
    for x in range(start_row, start_row+3):
        for y in range(start_col, start_col+3):
            if board[x][y] == num:
                return False
    
    return True

#Find next 0 in board
def next_blank(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None
#Solves the board using backtracking algorithm
def solve_board(board):
    grid_square = next_blank(board)

    #Base case, board is solved
    if grid_square == None:
        return True

    else:
        #Try every number from 1-9
        for num in range(1,10):
            #If valid move, try this path to a solution
            if check_move(board, grid_square, num):
                board[grid_square[0]][grid_square[1]] = num
                #All branches return true in a valid solution
                if(solve_board(board)):
                    return True
                #Else reset squares for another path
                board[grid_square[0]][grid_square[1]] = 0
        #No solutions possible in current state
        return False