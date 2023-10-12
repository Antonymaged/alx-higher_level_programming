#!/usr/bin/python3
"""JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Python object from a JSON file"""
    with open(filename) as fil:
        return json.load(fil)
