#!/usr/bin/python3
"""class Square"""


class Square:

    """Instantiation with optional size"""

    def __init__(self, size=0):

        """square instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):

        """returns the current square area"""

        return (self.__size ** 2)
