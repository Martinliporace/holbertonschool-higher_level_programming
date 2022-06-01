#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n"""

    triangle = []

    for i in range(n):
        triangle.append([1])
        for j in range(len(triangle) - 1):
            triangle[i].append(1)
            if j != 0 and j != (n-1) and i != 0:
                triangle[i][j] = ((triangle[i-1][j-1]) + (triangle[i-1][j]))

    return(triangle)
