#!/usr/bin/python3
    """read file"""


def read_file(filename=""):
    """READ_FILE"""
    with open(filename, "r", encoding="utf-8") as fil:
        print(fil.read(), end="")
