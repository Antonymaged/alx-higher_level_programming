#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    leng = len(my_list)-1
    new_lis = my_list.copy()
    if idx > leng or idx < 0:
        return (new_lis)
    else:
        new_lis[idx] = element
        return (new_lis)
