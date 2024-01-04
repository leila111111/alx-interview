#!/usr/bin/python3
''' module for pascal triangle'''


def pascal_triangle(n):
    '''implementation of pascal's triangle'''
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        start = [1]
        for j in range(1, i):
            start.append(triangle[i-1][j-1] + triangle[i-1][j])
        start.append(1)
        triangle.append(start)

    return triangle
