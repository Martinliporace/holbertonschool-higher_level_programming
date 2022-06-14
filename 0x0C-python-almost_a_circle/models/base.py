#!/usr/bin/python3
"""Base class"""
import json
import csv
from os import path


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == "Square":
            dummy = cls(17)
        elif cls.__name__ == "Rectangle":
            dummy = cls(17, 17)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances """

        j_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename) as f:
                for objs in cls.from_json_string(f.read()):
                    j_list.append(cls.create(**objs))
                return j_list
        except Exception:
            return j_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """returns an instance with all attributes already set"""
        with open(cls.__name__ + ".csv", "w", newline='') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            if list_objs is not None:
                for model in list_objs:
                    writer.writerow(model.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ returns a list of instances"""
        if path.exists(cls.__name__ + ".csv") is False:
            return []
        with open(cls.__name__ + ".csv", "r", newline='') as f:
            listofinstances = []
            reader = csv.DictReader(f)
            for row in reader:
                for key, value in row.items():
                    row[key] = int(value)
                listofinstances.append(cls.create(**row))
        return listofinstances
