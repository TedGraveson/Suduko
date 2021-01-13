#This file contains methods to create solutions for valid Suduko puzzles passed as 2-D arrays
#Solver inspired by https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

#Checks if a move is valid (no other instance of 'num' in respective row, column, and box)
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

    #First row and column of 3x3 box that contains the position to be checked
    start_row = (row // 3 ) * 3
    start_col = (col // 3) *3

    for x in range(start_row, start_row+3):
        for y in range(start_col, start_col+3):
            if board[x][y] == num:
                return False
    
    #Move is valid since 'num' was unique
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

    #Position for square being changed
    grid_square = next_blank(board)

    #Base case, board is solved
    if grid_square == None:
        return True

    else:
        #Try a number from 1-9
        for num in range(1,10):
            #Check if number is valid in that square
            if check_move(board, grid_square, num):
                #Change board to reflect this, and follow this decicision to a potential solution
                board[grid_square[0]][grid_square[1]] = num

                #Next empty spot tried with a number between 1-9
                if solve_board(board):
                    return True

                #Spot reset if board cannot be fully solved with number in this spot
                board[grid_square[0]][grid_square[1]] = 0

        #No solutions possible in current state, try another number in last call
        return False