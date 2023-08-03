#!/usr/bin/python3

  """
    Method: nqueens - place n queens
            on an n by n board so that
            no queens are attacking any
            others.
    Parameters: n is an int that sets
                board size and # of queens
    Return: All possible solutions to
            placement, in list of lists 

    """


def nqueens(n):
    """
 
     if n < 4:
        print("N must be at least 4")
        exit(1)
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve(board, 0, solutions)
    return solutions


def solve(board, row, solutions)

    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row + 1, solutions)
            board[row][col] = 0


def is_safe(board, row, col):
    

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i in range(row):
        for j in range(n):
            if board[i][j] == 1 and col - j == row - i or col + j == row - i:
                return False

    return True

if __name__ == "__main__":
    n = int(input("Enter N: "))
    solutions = nqueens(n)
    for solution in solutions:
        print(solution)