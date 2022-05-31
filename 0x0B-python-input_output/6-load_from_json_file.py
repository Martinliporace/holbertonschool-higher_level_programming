#!/usr/bin/python3
"""Read file"""


def load_from_json_file(filename):
    """function that reads a text file (UTF8) and prints it to stdout"""
    import json
    with open(filename, encoding="utf-8") as f:
        return (json.loads(f.read()))
