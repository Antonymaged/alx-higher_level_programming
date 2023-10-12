#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """Print the contents of file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
