#!/usr/bin/python3
"""Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class"""
    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area"""
        return(self.__size ** 2)

    def __str__(self):
        """str"""
        return("[Rectangle] {}/{}".format(self.__size, self.__size))
