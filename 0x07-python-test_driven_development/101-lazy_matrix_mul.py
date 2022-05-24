#!/usr/bin/python3
""" Lazy matrix multiplication """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices by using the module NumPy"""
    return(np.matmul(m_a, m_b))
