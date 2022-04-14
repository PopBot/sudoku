from src.sudoku import *


if __name__ == '__main__':

    board, leftovers, iterations = generate_sudoku_board()
    print('===========================================================')
    print('Sudoku board:')
    for row in board:
        print('\n')
        for col in row:
            print(col, end='    ')

    print('\n\nNumber of iterations:', iterations)
    print('===========================================================')
