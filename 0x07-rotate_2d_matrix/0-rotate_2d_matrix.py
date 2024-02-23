#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate a matrix"""
    rotation = [list(row) for row in matrix]
    n = len(matrix)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            matrix[i][n - 1 - j] = rotation[j][i]
