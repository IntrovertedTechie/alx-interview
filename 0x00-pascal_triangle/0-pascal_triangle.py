#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of size n.

    Args:
        n (int): Size of the triangle.

    Returns:
        list: Returns an empty list if n <= 0 or a list of lists of integers representing Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

