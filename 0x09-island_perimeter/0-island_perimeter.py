#!/usr/bin/python3
"""Island perimeter.
"""


def island_perimeter(grid):
    """function def island_perimeter(grid): that returns the perimeter of the island
    described in grid
    """
    perimeter = 0
    for i, k in enumerate(grid):
        for j, l in enumerate(k):
            if l == 0:
                continue
            routes = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == len(k) - 1 or (len(k) > j + 1 and k[j + 1] == 0),
                i == len(grid) - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or k[j - 1] == 0,
            )
            perimeter += sum(routes)
    return perimeter
