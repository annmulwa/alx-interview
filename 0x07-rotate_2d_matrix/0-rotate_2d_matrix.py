#!/usr/bin/python3
"""
Rotate 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Matrix must be edited in-place.
    """
    m = len(matrix)
    for i in range(int(m / 2)):
        y = (m - i - 1)
        for j in range(i, y):
            x = (m - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
