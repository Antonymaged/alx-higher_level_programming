#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newd = a_dictionary.copy()
    listk = list(newd.keys())
    for i in listk:
        newd[i] *= 2
    return (newd)
