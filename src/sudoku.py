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


def gen_possibilities():
    """
    Creates 3 x [1, 2, 3, 4, 5, 6, 7, 8, 9] list to track the
    row, column, and square possibilities.
    :return:
    """
    return [[i + 1 for i in range(9)] for _ in range(3)]


def generate_possibility_board(size=9):
    """
    Generate a possibility board.
    """
    # Generate a 9 x 9 board where each item contains 3 lists:
    #   1. Row values available
    #   2. Col values available
    #   3. Square values available
    return [[gen_possibilities() for _ in range(size)] for _ in range(9)]


def gen_stuff():
    possibilities = [[i for i in range(9)] for j in range(9)]
    # print(possibilities)
    for row in range(9):
        for col in range(9):
            possibilities[row][col] = generate_possibility_board(9)
    return possibilities


def generate_diagonals():
    return [i + 1 for i in range(9)]


def find_possible_number(possibilities, row, col, value):
    """
    Find the possible number for the row, column, and square.
    """
    for i in range(9):
        if possibilities[row][col][i][value - 1] == value:
            return i
    return None


def remove_possible_number(possibilities, row, col, value):
    """
    Remove the possible number for the row, column, and square.
    """
    for i in range(9):
        if possibilities[row][col][i][value - 1] == value:
            possibilities[row][col][i].remove(value)
            return True
    return False


def search_for_potential_number(arrays):
    # This function takes in three arrays of [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # and returns a random value that is in all three arrays.
    # If there is no value in all three arrays, it returns None.
    # This function is used to find a potential number for a cell.
    # It is used in the backtracking algorithm.

    # get a random int between 1 and 9
    while True:
        rand_int = random.randint(1, 9)
        if rand_int in arrays[0] and rand_int in arrays[1] and rand_int in arrays[2]:
            return rand_int


def generate_sudoku_board():
    count_iterations = 0
    board = generate_empty_sudoku_board(9)  # Creates a 9 x 9 board
    possibility_board = generate_possibility_board()
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                number = search_for_potential_number(possibility_board[row][col])
                board[row][col] = number
                # Remove the number for the row possibilities
                # TODO: Properly remove numbers from possibility_board
                remove_possible_number(possibility_board, row, col, number)
                count_iterations += 1
    return board, possibility_board, count_iterations
