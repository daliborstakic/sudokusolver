# The board itself, semi-changeable
board = [
    [0, 3, 0, 5, 0, 1, 9, 0, 6],
    [0, 4, 7, 9, 0, 0, 0, 2, 0],
    [6, 9, 0, 0, 4, 2, 5, 0, 3],
    [0, 6, 0, 0, 0, 9, 0, 3, 4],
    [0, 2, 0, 0, 0, 0, 8, 1, 0],
    [0, 7, 3, 1, 0, 0, 6, 9, 2],
    [4, 0, 0, 0, 2, 6, 3, 0, 0],
    [0, 1, 0, 0, 9, 5, 2, 0, 0],
    [0, 5, 2, 0, 0, 0, 0, 0, 0]
]


# Simple function to print the board in a Sudoku like characteristic
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Finds empty space, in this case a zero
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # Rows and columns


print_board(board)
