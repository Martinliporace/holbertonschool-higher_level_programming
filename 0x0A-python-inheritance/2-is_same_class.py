#!/usr/bin/python3
""" Exact same object"""

def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified
    class ; otherwise False."""
    result = False
    if type(obj) == a_class:
        result = True
    return(result)
