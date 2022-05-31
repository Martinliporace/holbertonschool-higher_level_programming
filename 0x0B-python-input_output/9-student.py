#!/usr/bin/python3
""" Class to JSON"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """str"""
        err = 'self.first_name, self.last_name, self.age'
        return "[Student] {} - {:d}".format(err)

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
