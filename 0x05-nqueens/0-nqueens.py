#!/usr/bin/python3
"""N Queens"""
import sys


def nqueens(n, y_axis, board):
    """
    Method: nqueens - place n queens
            on an n by n board
    """
    for x_axis in range(n):
        hold = 0
        for queen in board:
            if x_axis == queen[1]:
                hold = 1
                break
            if y_axis - x_axis == queen[0] - queen[1]:
                hold = 1
                break
            if x_axis - queen[1] == queen[0] - y_axis:
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