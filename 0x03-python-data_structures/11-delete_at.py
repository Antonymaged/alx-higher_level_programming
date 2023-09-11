#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    leng = len(my_list)
    if idx > leng or idx < 0:
        return(my_list)
    else:
        del(my_list[idx]i)
        return(my_list)
