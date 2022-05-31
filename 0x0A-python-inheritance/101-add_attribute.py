#!/usr/bin/python3
"""Can I?"""


def add_attribute(mc, varKey, varValue):
    """function that adds a new attribute to an object if it's possible"""

    if hasattr(mc, '__dict__'):
        setattr(mc, varKey, varValue)
    else:
        raise TypeError("can't add new attribute")
