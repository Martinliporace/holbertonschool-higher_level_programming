#!/usr/bin/python3
"""Student to disk and reload"""


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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        if attrs is not None:
            newDict = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__

            for j in attrs:
                if j in self.__dict__:
                    newDict[j] = self.__dict__[j]

            return newDict

        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for i in json:
            self.__dict__.update({i: json[i]})
