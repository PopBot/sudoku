from src.sudoku import *
import datetime


if __name__ == '__main__':
    # start_time = datetime.datetime.now()
    # sudoku_board, remaining_numbers, count_iterations = generate_sudoku_board_iteration_loop()
    # end_time = datetime.datetime.now()
    # print('===========================================================')
    # print('Sudoku board:')
    # for row in sudoku_board:
    #     print('\n')
    #     for col in row:
    #         print(col, end='    ')
    #
    # print("\n\nRemaining numbers:")
    # print(remaining_numbers)
    # print('\n\nNumber of iterations:', count_iterations)
    #
    # print("\n\nTime taken: {}".format(end_time - start_time))
    # print(generate_possibility_board())
    print(generate_diagonals())

    possibilities = generate_possibility_board()
    for row in possibilities:
        for col in row:
            print(col, end='    ')
        print('\n')

    # stuff = gen_stuff()
    # for row in stuff:
    #     for col in row:
    #         print(col, end='\n')

    board, leftovers, iterations = generate_sudoku_board()
    print('===========================================================')
    print('Sudoku board:')
    for row in board:
        print('\n')
        for col in row:
            print(col, end='    ')

    print("\n\nRemaining numbers:")
    print(leftovers)
    print('\n\nNumber of iterations:', iterations)
    print('===========================================================')
