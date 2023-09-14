#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    lang = len(my_list)
    multiples = []
    for i in range(lang):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
