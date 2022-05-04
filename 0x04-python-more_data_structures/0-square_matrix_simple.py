#!/usr/bin/python3

def mul(n):
    return n * n


def square_matrix_simple(matrix=[]):

    aux = matrix.copy()
    for i in range(len(matrix)):
        aux[i] = list(map(mul, matrix[i]))

    return(aux)
