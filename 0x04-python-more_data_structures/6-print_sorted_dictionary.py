#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_t = list(a_dictionary.keys())
    list_t.sort()
    for i in list_t:
        print("{}: {}".format(i, a_dictionary.get(i)))
