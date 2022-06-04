#!/usr/bin/python3
"""Base class"""
import json

class Base:
    """This class will be the "base" of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""

        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
                return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            j_list = []
            if list_objs is not None:
                for i in list_objs:
                    j_list.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(j_list))
            else:
                f.write(cls.to_json_string(j_list))