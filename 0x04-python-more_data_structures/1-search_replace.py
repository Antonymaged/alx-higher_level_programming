#!/usr/bin/python3


def search_replace(my_list, search, replace):
    le = len(my_list)
    for i in range(0, le):
        if my_list[i] == search:
            my_list[i] = replace
    return(my_list)
