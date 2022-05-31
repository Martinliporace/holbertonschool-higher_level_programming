#!/usr/bin/python3
"""Save Object to a file"""


def save_to_json_file(my_obj, filename):

    """function that writes an Object to a text file,
    using a JSON representation"""

    import json

    with open(filename, 'w', encoding="utf-8") as f:
        textJ = json.dumps(my_obj)
        ret = f.write(textJ)
