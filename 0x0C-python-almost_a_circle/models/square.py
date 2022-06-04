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
    def size(self, size):
        """ size setter """

        self.width = size
        self.height = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.size))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute."""

        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("size", args[1])
                self.size = args[1]
            if len(args) > 2:
                self.xy_validator("x", args[2])
                self.x = args[2]
            if len(args) > 3:
                self.xy_validator("y", args[3])
                self.y = args[3]

        else:
            if kwargs is not None and len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    if key == 'size':
                        self.integer_validator("size", value)
                    if key == 'x':
                        self.xy_validator("x", value)
                    if key == 'y':
                        self.xy_validator("y", value)
                    setattr(self, key, value)

    def to_dictionary(self):
        dic = {'id':self.id, 'size':self.size,
               'x':self.x, 'y':self.y}
        return(dic)
