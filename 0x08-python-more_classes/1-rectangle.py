#!/usr/bin/python3
"""defines a square"""


class Rectangle:

    """Instantiation with optional width and height"""

    def __init__(self, width=0, height=0):
        """rectangle instance"""

        self.width = width
        self.height = height

    @property
    def height(self):
        """retrieves height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    @property
    def width(self):
        """retrieves width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """sets width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value
