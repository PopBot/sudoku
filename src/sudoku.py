import math
import random


def generate_empty_sudoku_board(size=9):
    """
    Generate an empty sudoku board.
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
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


def get_possible_numbers(x, y, board, size=9):
    """
    Get the possible numbers for the board programmatically.
    In the future will try to use memoization to store numbers already placed.
    """
    numbers = [i for i in range(1, size+1)]
    for i in range(size):
        # Check the row
        if board[x][i] in numbers:
            numbers.remove(board[x][i])
        # Check the column
        if board[i][y] in numbers:
            numbers.remove(board[i][y])
        # Check the square
        if board[x//get_square_root(size)*get_square_root(size) + y//get_square_root(size)][i] in numbers:
            numbers.remove(board[x//get_square_root(size)*get_square_root(size) + y//get_square_root(size)][i])
    return numbers


def get_next_empty_cell(board, size=9):
    """
    Get the next empty cell.
    """
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return i, j
    return None, None


def solve_sudoku(board, size=9):
    """
    Solve the sudoku board.
    """
    x, y = get_next_empty_cell(board, size)
    if x is None:
        return True
    for i in get_possible_numbers(x, y, board, size):
        board[x][y] = i
        if solve_sudoku(board, size):
            return True
        board[x][y] = 0
    return False


def make_sudoku_column_row_board(size=9):
    """
    Generate size by size board
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]
    """
    return [[i + 1 for i in range(size)] for j in range(size)]


def generate_sudoku_board_iteration_loop(size=9):
    count_iterations = 0
    board = generate_empty_sudoku_board(size)
    potential_numbers = make_sudoku_column_row_board(size)
    for i in range(size):
        selected_row = random.randint(0, size-1)
        col_numbers_left = [i + 1 for i in range(size)]
        row_numbers_left = [i + 1 for i in range(size)]
        square_numbers_left = [i + 1 for i in range(size)]
        for j in range(size):
            if board[i][j] == 0:
                possible_numbers = get_possible_numbers(i, j, board, size)
                chosen_number = random.choice(possible_numbers)
                board[i][j] = random.choice(possible_numbers)
                potential_numbers[i].remove(board[i][j])
                count_iterations += 1
    return board, potential_numbers, count_iterations


def generate_sudoku_board_seed_method(size=9):
    """
    This version attempts to place "seed" numbers on the board and then fill in the rest by checking.
    :param size:
    :return:
    """
    board = generate_empty_sudoku_board(size)
    squares = [[i + 1 for i in range(size)] for j in range(size)]
    return squares
