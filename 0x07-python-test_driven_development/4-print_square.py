#!/usr/bin/python3

"""
size is the size length of the square
size must be an integer
if size is less than 0, raise a ValueError
"""


def print_square(size):

    """function that prints a square with the character #"""

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    else:
        for i in range(0, size):
            for j in range(size):
                print("#", end='')
            print()
