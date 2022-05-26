#!/usr/bin/python3
"""
matrix must be a list of lists of integers or floats
"""


def matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices"""
    err1 = 'm_a must be a list of lists or m_b must be a list of lists'
    err2 = 'm_b must be a list of lists or m_b must be a list of lists'

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    if len(m_a) == 0 or (len(m_a) > 0 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) > 0 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if type(i) is not list:
            raise TypeError(err1)

        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_a should contain only integers or floats')
        sizeA = len(m_a[0])
        if len(i) != sizeA:
            raise TypeError('each row of m_a must be of the same size')

    for ii in m_b:
        if type(ii) is not list:
            raise TypeError(err1)

        for j in ii:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_b should contain only integers or floats')
        sizeB = len(m_b[0])
        if len(ii) != sizeB:
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b) or len(m_a) == 0 and len(m_b) == 0:
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for i in range(len(m_a)):
        m_c.append([0, 0])
    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                m_c[x][y] += m_a[x][z] * m_b[z][y]
    return m_c
