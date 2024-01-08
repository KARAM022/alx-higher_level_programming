#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = 0
    res = []
    for i in my_list:
        if i % 2 == 0:
            res.append(True)
        else:
            res.append(False)
        j += 1
    return res
