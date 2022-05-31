#!/usr/bin/python3
"""My integer"""


class MyInt(int):

    def __eq__(self, other):
        """ == comparator """

        return False

    def __ne__(self, other):
        """ != comparator """

        return True
