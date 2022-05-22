#!/usr/bin/python3

def matrix_divided(matrix, div):
    newMatrix = []
    err = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(matrix) is not list:
        raise TypeError(err)

    size = len(matrix[0])
    for x in matrix:
        if len(x) != size:
            raise TypeError('Each row of the matrix must have the same size')
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError(err)

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in matrix:
        newMatrix.append(list(map(lambda x: round(x / div, 2), i)))
    return(newMatrix)
