#!/usr/bin/python3

"""
0-island_perimeter module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list[list[int]]): 2D grid representing the island.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Each land cell contributes 4 edges

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Deduct 2 edges (shared edge)

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Deduct 2 edges (shared edge)

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
