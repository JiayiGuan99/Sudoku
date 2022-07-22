"""

@author: Jiayi Guan

@references: https://www.101computing.net/sudoku-generator-algorithm/
"""
from random import randint, shuffle

sudoku_board = [
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

# function to print the board nicely
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:       
                print(" | ", end = "")
                print(str(board[i][j]) + " ", end = "")
            elif j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end = "")

# find an empty slot
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

#check if the number is valid to put in
def valid(board, num, position):
    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False
        
    #check column
    for i in range(len(board[0])):
        if board[i][position[1]] == num and position[0] != i:
            return False
        
    #check 3x3 square
    # top 3 will be 00 01 02, middle 3 are 10 11 12, bottom 3 are 20 21 22
    box_x = position[1] // 3     # row
    box_y = position[0] // 3     # col
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False
    return True

def check_full(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == 0:
                return False
    return True


# recursively test different numbers and backtrack if needed
def solve(board):
    global counter
    for i in range(0,81):
        row = i // 9
        col = i % 9
        if board[row][col] == 0:
            for i in range(1,10):
                if valid(board, i, (row, col)):
                    board[row][col] = i
                    if check_full(board):
                        counter += 1
                        break
                    if solve(board):
                        return True
            break    
    board[row][col] = 0

#generate a full filled sudoku board 
def generate_full(board):
    global counter
    nums = [1,2,3,4,5,6,7,8,9]
    empty = find_empty(board)
    if empty:
        row, col = empty
    if board[row][col] == 0:
        shuffle(nums)      
        for i in nums:    
            if valid(board, i, (row, col)):
                board[row][col] = i
                if check_full(board):
                    return True
                if generate_full(board):
                    return True  
    board[row][col] = 0

# For Sudoku, suppose easy: 0-16 empty slots  medium: 17-33  hard 34-50
# remove n numbers and make sure there is only one unique solution
def remove(board, n):
    global counter
    while n > 0:
        # get position for a non zero number
        row = randint(0,8)
        col = randint(0,8)
        while board[row][col] == 0:
            row = randint(0,8)
            col = randint(0,8)
        temp = board[row][col]
        # remove it and check how many solutions are possible
        board[row][col] = 0
        temp_board = []
        for i in range(0,9):
            temp_board.append([])
            for j in range(0,9):
                temp_board[i].append(board[i][j])
        counter = 0
        solve(temp_board)
        # if not one unique solution, backtrack
        if counter != 1:
            board[row][col] == temp
        else:
            n -= 1
        
'''  
generate_full(sudoku_board)    
print_board(sudoku_board)
remove(sudoku_board, 33) 
print("\n")
print_board(sudoku_board)   
print(sudoku_board) '''