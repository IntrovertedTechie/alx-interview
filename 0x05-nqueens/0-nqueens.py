#!/usr/bin/python3
"""N Queens - A program to solve the N-Queens problem."""

import sys


def nqueens(n, y_axis, board):
    """
    Recursive function to find solutions to the N-Queens problem.
     Args:
        n (int): The size of the chessboard and the number of queens to place.
        y_axis (int): The current row in which we are trying to place a queen.
        board (list): List of lists representing the current board state.
    """
    for x_axis in range(n):
        hold = 0
        for queen in board:
            if x_axis == queen[1]
or y_axis - x_axis == queen[0] - queen[1]    
or x_axis - queen[1] == queen[0] - y_axis:
                hold = 1
                break
        if hold == 0:
            board.append([y_axis, x_axis])
            if y_axis != n - 1:
                nqueens(n, y_axis + 1, board)
            else:
                print(board)
            del board[-1]


def main():
    """
    Main function to handle user input and call the nqueens function.

    Usage: ./nqueens.py N

    Args:
        N (int): The size of the chessboard and the number of queens to place.

    Returns:
        None (prints the solutions directly).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n, 0, [])


if __name__ == '__main__':
    main()
