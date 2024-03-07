#!/usr/bin/python3
"""Island perimeter.
"""


def island_perimeter(grid):
    """function def island_perimeter(grid): that returns
    the perimeter of the island described in grid
    """
    perimeter = 0
    n = len(grid)
    for i, k in enumerate(grid):
        for j, tel in enumerate(k):
            if tel == 0:
                continue
            routes = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == len(k) - 1 or (len(k) > j + 1 and k[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or k[j - 1] == 0,
            )
            perimeter += sum(routes)
    return perimeter
