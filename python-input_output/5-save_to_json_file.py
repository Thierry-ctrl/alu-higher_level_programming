#!/usr/bin/python3
"""function that writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """using json"""
    with open(filename, "w+") as f:
        return json.dump(my_obj, f)
