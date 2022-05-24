#!/usr/bin/python3
"""
matrix must be a list of lists of integers or floats
"""


def matrix_mul(m_a, m_b):

    err1 = 'm_a must be a list of lists or m_b must be a list of lists'
    err2 = 'm_b must be a list of lists or m_b must be a list of lists'

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for i in m_a:
        if type(i) is not list:
            raise TypeError(err1)
        if not i:
            raise ValueError("m_a can't be empty")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_a should contain only integers or floats')
        sizeA = len(m_a[0])
        if len(i) != sizeA:
            raise TypeError('each row of m_a must be of the same size')

    for i in m_b:
        if type(i) is not list:
            raise TypeError(err1)
        if not i:
            raise ValueError("m_b can't be empty")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_b should contain only integers or floats')
        sizeB = len(m_b[0])
        if len(i) != sizeB:
            raise TypeError('each row of m_b must be of the same size')

    size_Ma = len(m_a[0])
    size_Mb = len(m_b)

    if size_Ma != size_Mb:
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for i in range(len(m_a)):
        m_c.append([0, 0])
    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                m_c[x][y] += m_a[x][z] * m_b[z][y]
    return m_c
