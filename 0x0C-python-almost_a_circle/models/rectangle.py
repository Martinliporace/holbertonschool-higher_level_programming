#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Write the class Rectangle that inherits from Base:

    In the file models/rectangle.py
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.xy_validator("x", x)
        self.__x = x
        self.xy_validator("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """sets width"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets height"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """retrieves x"""
        return(self.__x)

    @x.setter
    def x(self, value):
        """sets x"""
        self.xy_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """retrieves y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """sets y"""
        self.xy_validator("y", value)
        self.__y = value

    def area(self):
        """area value of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """print the rectangle with the character #"""

        for z in range(self.__y):
            print('')
        for x in range(self.__height):
            for y in range(self.__x):
                print(" ", end='')
            for i in range(self.__width):
                print('#', end='')
            print('')

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute."""

        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.integer_validator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.xy_validator("x", args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.xy_validator("y", args[4])
                self.__y = args[4]

        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'width':
                        self.integer_validator("width", value)
                    if key == 'height':
                        self.integer_validator("height", value)
                    if key == 'x':
                        self.xy_validator("x", value)
                    if key == 'y':
                        self.xy_validator("y", value)
                    setattr(self, key, value)

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def xy_validator(self, name, value):
        """xy validator"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return(dic)
