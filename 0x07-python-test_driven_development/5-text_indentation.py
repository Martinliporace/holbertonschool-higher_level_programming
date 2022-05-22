#!/usr/bin/python3
"""
text must be a string, otherwise raise a TypeError
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError('text must be a string')

    chars = ('. ', ': ', '? ')
    for x in chars:
        if x in text:
            text = text.replace(x, x[0] + '\n\n')

    print(text, end='')
