#!/usr/bin/python3
def uniq_add(my_list=[]):
    ul = set(my_list)
    num = 0

    for i in ul:
        num += i

    return (num)
