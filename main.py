import pyautogui as pg
import numpy as np
import generatePuzzle
import time

board = generatePuzzle.puzzle

# while True:
#     rows = list(input('Row: '))
#     ints = []
#     for n in rows:
#         ints.append(int(n))
#     board.append(ints)
#     if len(board)==9:
#         break
#     print('Row '+str(len(board)) + ' Complete')


def solve(grid):
    find=find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col]=i

            if solve(grid):
                return True
            grid[row][col]=0
    return False


# time.sleep(3)


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


def print_board(grid):
    for i in range(len(grid)):
        if i % 3==0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                return (i, j)
    return None


print_board(board)
solve(board)
print("  Finished solution  ")
print_board(board)
