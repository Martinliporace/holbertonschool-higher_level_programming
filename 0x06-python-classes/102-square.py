#!/usr/bin/python3
"""class Square"""


class Square:

    """Instantiation with optional size"""

    def __init__(self, size=0):

        """square instance"""
        self.size = size

    def area(self):

        """returns the current square area"""

        return (self.__size ** 2)

    @property
    def size(self):
        """retrieves size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def __eq__(self, other):
        """ == comparator """

        return self.area() == other.area()

    def __ne__(self, other):
        """ != comparator """

        return self.area() != other.area()

    def __gt__(self, other):
        """ > comparator """

        return self.area() > other.area()

    def __lt__(self, other):
        """ < comparator """

        return self.area() < other.area()

    def __ge__(self, other):
        """ >= comparator """

        return self.area() >= other.area()

    def __le__(self, other):
        """ <= comparator """

        return self.area() <= other.area()
