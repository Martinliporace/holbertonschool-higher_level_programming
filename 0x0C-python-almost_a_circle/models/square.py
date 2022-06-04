#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size setter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """

        self.integer_validator("width", value)
        self.width = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.size))