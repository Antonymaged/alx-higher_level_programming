#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listo = list(a_dictionary.keys())
    listo.sort()
    for i in listo:
        print("{}: {}".format(i, a_dictionary.get(i)))
