def generate_empty_sudoku_board():
    """
    Generate an empty sudoku board.
    """
    board = [[0 for i in range(9)] for j in range(9)]
    return board


def is_valid_number(x, y, board):
    """
    Check if the number is valid in the board.
    """
    for i in range(9):
        if board[x][i] == board[y][i]:
            return False
    for i in range(9):
        if board[x][i] == board[x//3*3 + y//3][i]:
            return False
    return True

