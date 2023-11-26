import numpy as np
import random


# board = [[0] * 9 for _ in range(9)]

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                random.shuffle(arr)
                for num in arr:
                    if valid(board, num, (row, col)):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)

    # Remove some cells to create the puzzle
    num_to_remove = random.randint(40, 50)  # Adjust the range as desired
    for _ in range(num_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0
    return board


def valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i]==num and pos[1]!=i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if grid[i][j]==num and (i, j)!=pos:
                return False
    return True


puzzle=generate_sudoku()
print(puzzle)

