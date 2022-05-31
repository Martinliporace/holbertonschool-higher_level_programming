#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, other):
        """ == comparator """

        return False

    def __ne__(self, other):
        """ != comparator """

        return True
