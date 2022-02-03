# make board
# get blank boxes
# insert a number
# check row and column for correctness


sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]

]


def solution(board):

    empty = get_empty(board)
    if not empty:
        return True  # solved
    else:
        row, col = empty
    for i in range(1, 10):
        if check_correct(board, i, (row, col)):
            board[row][col] = i

            if solution(board):
                return True
            board[row][col] = 0

    return False


def check_correct(board, num, pos):

    #pos----row , column
    # check number in row
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check number in column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check the 3*3 box    #x---col , y---row
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def get_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if sudoku_board[i][j] == 0:
                return i, j

    return None


def show_board(board):
    for i in range(len(sudoku_board)):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j in range(len(sudoku_board)):
            if j % 3 == 0 and j != 0:
                print('|', end='')
            print(sudoku_board[i][j], end=' ')
        print()


show_board(sudoku_board)
solution(sudoku_board)
print("after solving")
show_board(sudoku_board)
