#!/usr/bin/python3
"""class Square"""


class Square:

    """Instantiation with optional size"""

    def __init__(self, size=0, position=(0, 0)):

        """square instance"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """sets position"""

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):

        """prints square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for x in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()

    def __str__(self):
        """prints square"""
        out = ""

        if self.size == 0:
            return (out)

        for i in range(self.position[1]):
            out += '\n'

        for i in range(0, self.size):
            for x in range(self.position[0]):
                out += ' '
            for j in range(self.size):
                out += '#'

            if i is not (self.size - 1):
                out += "\n"

        return (out)
