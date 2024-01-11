#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    lk = list(new.keys())

    for i in lk:
        new[i] *= 2

    return (new)
