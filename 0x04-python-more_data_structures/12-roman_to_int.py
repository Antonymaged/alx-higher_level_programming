#!/usr/bin/python3
def to_sub(listn):
    tosub = 0
    maxli = max(listn)
    for n in listn:
        if maxli > n:
            tosub += n
    return (maxli - tosub)
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listk = list(rom.keys())
    n = 0
    lastrom = 0
    listn = [0]
    for ch in roman_string:
        for r_num in listk:
            if r_num == ch:
                if rom.get(ch) <= lastrom:
                    n += to_sub(listn)
                    listn = [rom.get(ch)]
                else:
                    listn.append(rom.get(ch))
                lastrom = rom.get(ch)
    num += to_subtract(listn)
    return (n)
