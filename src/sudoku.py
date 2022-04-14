import math


def generate_empty_sudoku_board(size=9):
    """
    Generate an empty sudoku board.
    """
    if not check_if_perfect_square(size):
        raise Exception("The size of the board must be a perfect square.")
    board = [[0 for i in range(size)] for j in range(size)]
    return board


def is_valid_number(x, y, board, size=9):
    """
    Check if the number is valid in the board.
    """
    for i in range(size):
        if board[x][i] == board[y][i]:
            return False
    for i in range(size):
        if board[x][i] == board[x//get_square_root(size)*get_square_root(size) + y//get_square_root(size)][i]:
            return False
    return True


def is_valid_board(board, size=9):
    """
    Check if the board is valid.
    """
    for i in range(get_square_root(size)):
        for j in range(get_square_root(size)):
            if board[i][j] != 0:
                if not is_valid_number(i, j, board):
                    return False
    return True


def check_if_perfect_square(n):
    """
    Check if the number is a perfect square.
    """
    return int(math.sqrt(n))**2 == n


def get_square_root(n):
    """
    Get the square root of the number.
    """
    return int(math.sqrt(n))

