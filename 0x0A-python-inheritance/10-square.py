#!/usr/bin/python3
"""Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """class"""
    def __init__(self, size):
        """init"""
        self.__size = size

    def area(self):
        """area"""
        return(self.__size * self.__size)

    def __str__(self):
        """str"""
        return("[Rectangle] {}/{}".format(self.__size, self.__size))
