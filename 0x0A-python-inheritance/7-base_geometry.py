#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry():
    """class"""
    pass

    def area(self):
        """raises an Exception with the message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
