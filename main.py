# The board itself, semi-changeable
board = [
    [1, 3, 0, 8, 6, 5, 0, 4, 9],
    [0, 9, 8, 3, 7, 0, 0, 1, 0],
    [0, 0, 4, 0, 2, 9, 0, 0, 8],
    [3, 0, 9, 5, 0, 1, 0, 7, 6],
    [0, 7, 0, 2, 0, 6, 0, 0, 0],
    [2, 0, 6, 7, 4, 0, 0, 0, 1],
    [4, 2, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 9, 0, 0, 0, 2, 4]
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


# Checks if the entered number is valid or not
def is_valid(board, num, pos):
    # Checking row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking columns
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking 3x3 boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


print_board(board)
solve(board)
print("\n")
print_board(board)
