from src.sudoku import *


if __name__ == '__main__':
    board = generate_empty_sudoku_board()
    print(board[3][4])
    print(generate_empty_sudoku_board())
    print(get_possible_numbers(3, 4, board))
    print(generate_sudoku_board_seed_method())
